import os
import yaml
from psycopg2 import connect

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
                fieldType += "("+str(field["length"])+")"

            if field["pk"]:
                tablePK.extend([field["name"]])

            fieldFK = ""

            if field["fk"]:
                fieldFK = "references "+str(field["fk"])

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
            base_query +=  ");"

        query = base_query.format(tableName=table["name"], queryParts=",\n\t".join(queryParts), tablePK=", ".join(tablePK))

        # CREATE TABLE
        try:
            print("Creating Table: "+table["name"])
            cursor.execute(query)
        except Exception as e:
            print(e)
            conn.rollback()
        else:
            # no errors!
            conn.commit()

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


    status_data_query = """INSERT INTO business_status(cd_status, description) VALUES """
    for i, row in enumerate(status):
        row_query = "('{}', '{}')".format(row[0], row[1])
        if i < len(status) - 1:
            row_query += ','
        status_data_query += row_query
    q_list.append((status_data_query, 'Adding Status Data)'))

    subtype_data_query = """INSERT INTO business_subtype(cd_subtype, description) VALUES """
    for i, row in enumerate(types):
        row_query = "('{}', '{}')".format(row[0], row[1])
        if i < len(types) - 1:
            row_query += ','
        subtype_data_query += row_query
    q_list.append((subtype_data_query, 'Adding Subtype Data)'))

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

