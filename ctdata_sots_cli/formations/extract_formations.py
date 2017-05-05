from psycopg2 import connect, DataError, IntegrityError

EXTRACT_FORMATIONS_QUERY = """
    SELECT
        master.id_bus,
        filing.id_bus_flng,
        EXTRACT(YEAR FROM filing.dt_filing) AS year,
        EXTRACT(MONTH FROM filing.dt_filing) AS month,
        fips.town,
        master.cd_status,
        status.description,
        subtypes.cd_subtype,
        subtypes.description,
        tx.type as type,
        CASE WHEN length(master.ad_city) > 0 then master.ad_city
         ELSE master.ad_mail_city
        END as city,
        CASE WHEN tx.stock = 'TRUE' then 'S'
         WHEN tx.nonstock = 'TRUE' then 'N'
         ELSE ''
        END as stock,
        CASE WHEN tx.domestic = 'TRUE' then 'D'
         WHEN tx.foreign = 'TRUE' then 'F'
         ELSE ''
        END as domestic
    FROM
        bus_filing AS filing
        JOIN bus_master AS master ON master.id_bus = filing.id_bus
        JOIN tx_codes AS tx ON tx.cd_trans_type = filing.cd_trans_type
        JOIN fips AS fips ON TRIM(BOTH FROM LOWER(
        CASE WHEN length(master.ad_city) > 0 then master.ad_city
         ELSE master.ad_mail_city END)) = LOWER(fips.subtown)
        JOIN business_subtype AS subtypes ON subtypes.cd_subtype = TRIM(BOTH FROM master.cd_subtype)
        JOIN business_status AS status ON status.cd_status = TRIM(BOTH FROM master.cd_status)
    WHERE
        tx.label ILIKE '%formation%'
        AND (master.ad_st = 'CT' OR master.ad_mail_st = 'CT')
    ORDER BY
        year ASC,
        month ASC,
        town ASC,
        cd_status ASC,
        cd_subtype ASC
"""

def connectDB(db, user, pwd, host, port):
    """Opens a psycopg2 db connction using configuration parems set in self.scriptVars."""
    conn = connect(database=db, user=user, password=pwd, host=host, port=port)
    cursor = conn.cursor()
    return conn, cursor


def extract(db, user, pwd, host, port, outfile):
    conn, cursor = connectDB(db, user, pwd, host, port)
    outputquery = 'copy ({0}) to stdout with csv header'.format(EXTRACT_FORMATIONS_QUERY)

    with open(outfile, 'w') as f:
        cursor.copy_expert(outputquery, f)