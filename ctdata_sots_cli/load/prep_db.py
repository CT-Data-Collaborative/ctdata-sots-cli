import os
import yaml
from psycopg2 import connect, DataError, IntegrityError

from ctdata_sots_cli.data import tx_codes, fips

def connectDB(db, user, pwd, host, port):
    """Opens a psycopg2 db connction using configuration parems set in self.scriptVars."""
    conn = connect(database=db, user=user, password=pwd, host=host, port=port)
    cursor = conn.cursor()
    return conn, cursor


def dropTables(conn, cursor, schemapath):
    """Drop all tables as specified in schema."""

    with open(os.path.join(schemapath, 'structure.yml'), 'r') as f:
        structure = yaml.load(f.read())

    for table in structure["tables"]:
        query = """DROP TABLE IF EXISTS {} CASCADE;""".format(table['name'])
        try:
            print("Dropping Table: " + table["name"])
            cursor.execute(query)
        except Exception as e:
            print(e)
            conn.rollback()
        else:
            # no errors!
            conn.commit()
    for table in ['business_subtype', 'business_status', 'tx_codes', 'fips', 'full_text_index']:
        query = """DROP TABLE IF EXISTS {} CASCADE;""".format(table)
        try:
            print("Dropping Table: " + table)
            cursor.execute(query)
        except Exception as e:
            print(e)
            conn.rollback()
        else:
            # no errors!
            conn.commit()


def buildTables(conn, cursor, schemapath):
    """Read schema files and build tables.

        Args:
            dry (Optional[boolean]): output query strings but do not execute or commit
            fk (Optionan[boolean]): build foreign keys using schema definitions
    """

    with open(os.path.join(schemapath, 'structure.yml'), 'r') as f:
        structure = yaml.load(f.read())

    for table in structure["tables"]:
        # GENERATE QUERY
        queryParts = []
        schema_file_name = "{}.yml".format(table['name'])
        with open(os.path.join(schemapath, schema_file_name), 'r') as f:
            schema = yaml.load(f.read())

        tablePK = ['PRIMARY_ID']
        for field in schema['fields']:
            fieldType = field["type"]

            ## Use supplied types.
            if field["type"] == "char":
                fieldType += "(" + str(field["length"]) + ")"

            if field["pk"]:
                tablePK.extend([field["name"]])

            fieldFK = ""

            if field["fk"]:
                fieldFK = "references " + str(field["fk"])

            fieldDef = " ".join([field["name"], fieldType, fieldFK]).strip()
            queryParts.extend([fieldDef])
        queryParts.extend(['PRIMARY_ID UUID'])

        base_query = """CREATE TABLE IF NOT EXISTS {tableName} (
        {queryParts},
        PRIMARY KEY ({tablePK})"""

        if table['name'] == 'BUS_MASTER':
            base_query += ", UNIQUE (ID_BUS));"
        # elif table['name'] == 'BUS_FILING':
        #     base_query += ", UNIQUE (ID_BUS_FLNG));"
        else:
            base_query += ");"

        query = base_query.format(tableName=table["name"], queryParts=",\n\t".join(queryParts),
                                  tablePK=", ".join(tablePK))

        # CREATE TABLE
        try:
            print("Creating Table: " + table["name"])
            cursor.execute(query)
        except Exception as e:
            print(e)
            conn.rollback()
        else:
            # no errors!
            conn.commit()


def loadData(conn, cursor, schemapath, datapath):
    with open(os.path.join(schemapath, 'structure.yml'), 'r') as f:
        structure = yaml.load(f.read())
    for table in structure['tables']:
        table_name = table['name']
        table_file_name = "{}.csv".format(table_name)
        file_path = os.path.join(datapath, table_file_name)

        SQL_STATEMENT = """
            COPY {} FROM STDIN WITH
                CSV
                HEADER
                DELIMITER AS ','
                NULL as 'null'
            """.format(table_name)

        with open(file_path, 'rb') as file:
            try:
                cursor.execute("SET datestyle to 'ISO,YMD';")
                cursor.copy_expert(sql=SQL_STATEMENT, file=file)
                # self._cursor.copy_from(file, table, sep=',')
                conn.commit()
                print("Loaded {} successfully.".format(table_name))
            except (DataError, IntegrityError) as e:
                conn.rollback()
                print(e)
                print(e.pgcode)
                print("...rolling back")


def buildStatusAndSubtypeTable(conn, cursor):
    q_list = []
    status = [('AC', 'Active'), ('CN', 'Cancelled'), ('CS', 'Consolidation'), ('CV', 'Converted'),
              ('D', 'Dissolved'),
              ('DS', 'Unknown'), ('ER', 'Expired Reservation'), ('EX', 'Expired'), ('FF', 'Forfeited'),
              ('M', 'Merged'),
              ('RC', 'Reserved Cancel'), ('RD', 'Redomesticated'), ('RG', 'Registered'), ('RN', 'Renunciated'),
              ('RS', 'Reserved'), ('WD', 'Withdrawn'), ('RV', 'Revoked'), ('W', 'W Second'), ('RE', 'Recorded'),
              ('PM', 'Pending Merger'), ('PC', 'Pending Conversion'), ('CO', 'Converted Out')]

    types = [('C', 'Corporation'), ('D', 'Domestic Limited Partnership'), ('F', 'Foreign Limited Partnership'),
             ('G', 'Domestic Limited Liability Company'), ('H', 'Foreign Limited Liability Company'),
             ('I', 'Domestic Limited Liability Partnership'), ('J', 'Foreign Limited Liability Partnership'),
             ('K', 'General Partnership'), ('L', 'Domestic Statutory Trust'), ('M', 'Foreign Statutory Trust'),
             ('O', 'Other'), (' ', 'Unknown'), ('P', 'Domestic Stock Corporation'),
             ('Q', 'Foreign Stock Corporation'),
             ('R', 'Domestic Non-Stock Corporation'), ('S', 'Foreign Non-Stock Corporation'), ('T', 'All Entities'),
             ('U', 'Domestic Credit Union Stock'), ('V', 'Domestic Credit Union Non-Stock'),
             ('W', 'Domestic Bank Stock'), ('X', 'Domestic Bank Non-Stock'), ('Y', 'Domestic Insurance Stock'),
             ('Z', 'Domestic Insurance Non-Stock'), ('B', 'Benefit Corporation')]


    status_table_query = """CREATE TABLE IF NOT EXISTS business_status (
        cd_status character varying PRIMARY KEY,
        description character varying);"""

    q_list.append((status_table_query, 'Creating Table: Business Status'))

    subtype_table_query = """CREATE TABLE IF NOT EXISTS business_subtype (
        cd_subtype character varying PRIMARY KEY,
        description character varying);"""

    q_list.append((subtype_table_query, 'Creating Table: Business Subtype'))

    tx_codes_table_query = """CREATE TABLE IF NOT EXISTS tx_codes (
        cd_trans_type character varying PRIMARY KEY,
        label character varying,
        stock character varying,
        nonstock character varying,
        domestic character varying,
        foreign_company character varying,
        benefit character varying);"""

    q_list.append((tx_codes_table_query, 'Creating Table: Transaction Codes'))

    fips_table_query = """CREATE TABLE IF NOT EXISTS fips (
        town character varying,
        fips character varying,
        county_fips character varying,
        county character varying,
        subtown character varying);"""

    q_list.append((fips_table_query, 'Creating Table: FIPS'))

    status_data_query = """INSERT INTO business_status(cd_status, description) VALUES """
    for i, row in enumerate(status):
        row_query = "('{}', '{}')".format(row[0], row[1])
        if i < len(status) - 1:
            row_query += ','
        status_data_query += row_query
    q_list.append((status_data_query, 'Adding Status Data'))

    subtype_data_query = """INSERT INTO business_subtype(cd_subtype, description) VALUES """
    for i, row in enumerate(types):
        row_query = "('{}', '{}')".format(row[0], row[1])
        if i < len(types) - 1:
            row_query += ','
        subtype_data_query += row_query
    q_list.append((subtype_data_query, 'Adding Subtype Data'))

    tx_code_data_query = """INSERT INTO tx_codes(cd_trans_type, label, stock. nonstock, domestic, foreign, beneift, type) VALUES """
    for i, row in enumerate(tx_codes):
        row_query = "('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(row['cd_trans_type'], row['label'],
                                                                              row['stock'], row['nonstock'],
                                                                              row['domestic'],row['foreign_company'],
                                                                              row['benefit'])
        if i < len(tx_codes) - 1:
            row_query += ','
        tx_code_data_query += row_query
    q_list.append((tx_codes_table_query, 'Adding Transaction Codes'))

    fips_code_data_query = """INSERT INTO fips(town, fips, county_fips, county, subtown) VALUES"""
    for i, row in enumerate(fips):
        row_query = '("{}", "{}", "{}", "{}", "{}")'.format(row['town'], row['fips'], row['county_fips'], row['county'], row['subtown'])
        if i < len(fips) - 1:
            row_query += ','
        fips_code_data_query += row_query
    q_list.append((fips_code_data_query, 'Adding FIPS Data'))

    for query in q_list:
        # CREATE TABLE
        try:
            print(query[1])
            cursor.execute(query[0])
        except Exception as e:
            print(e)
            conn.rollback();
        else:
            # no errors!
            conn.commit()
