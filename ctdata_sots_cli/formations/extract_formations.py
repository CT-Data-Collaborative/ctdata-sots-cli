from psycopg2 import connect

STARTS_QUERY = """
SELECT bus_filing.cd_trans_type, bus_filing.dt_effect, 
  CASE 
    WHEN bus_filing.cd_trans_type = 'LC'    THEN 'Domestic Limited Liability Company'   	 
    WHEN bus_filing.cd_trans_type = 'CIS'   THEN 'Domestic Stock Corporation'	           
    WHEN bus_filing.cd_trans_type = 'CIN'   THEN 'Domestic Non-Stock Corporation'	       
    WHEN bus_filing.cd_trans_type = 'LLP'   THEN 'Domestic Limited Liability Partnership'
    WHEN bus_filing.cd_trans_type = 'LP'    THEN 'Domestic Limited Partnership'	         
    WHEN bus_filing.cd_trans_type = 'ST'    THEN 'Domestic Statutory Trust'	             
    WHEN bus_filing.cd_trans_type = 'BCORP' THEN 'Domestic Benefit Corporation'	         
    WHEN bus_filing.cd_trans_type = 'LCF'   THEN 'Foreign Limited Liability Company'      
    WHEN bus_filing.cd_trans_type = 'CFAS'  THEN 'Foreign Stock Corporation'              
    WHEN bus_filing.cd_trans_type = 'CFAN'  THEN 'Foreign Non-Stock Corporation'          
    WHEN bus_filing.cd_trans_type = 'LLPF'  THEN 'Foreign Limited Liability Partnership'  
    WHEN bus_filing.cd_trans_type = 'LPF'   THEN 'Foreign Limited Partnership'            
    WHEN bus_filing.cd_trans_type = 'STF'   THEN 'Foreign Statutory Trust'  
    ELSE 'No' END AS ENTITY_TYPE, 
    bus_master.nm_name, 
    date_part('year', dt_effect) AS year_effect, 
    date_part('month', dt_effect) AS month_effect  
FROM bus_filing
JOIN bus_master ON bus_filing.id_bus = bus_master.id_bus
WHERE 
  cd_trans_type IN ('LC', 'CIS', 'CIN', 'LLP', 'LP', 'ST', 'BCORP', 'LCF', 'CFAS', 'CFAN', 'LLPF', 'LPF', 'STF') --formations
ORDER BY 
  dt_effect DESC
"""

STOPS_QUERY = """
SELECT bus_filing.cd_trans_type, bus_filing.dt_effect, 
  CASE 
    WHEN bus_filing.cd_trans_type = 'LCD'   THEN 'Domestic Limited Liability Company'   
    WHEN bus_filing.cd_trans_type = 'CDRS'  THEN 'Domestic Stock Corporation'     
    WHEN bus_filing.cd_trans_type = 'CDRN'  THEN 'Domestic Non-Stock Corporation'
    WHEN bus_filing.cd_trans_type = 'LLPR'  THEN 'Domestic Limited Liability Partnership'
    WHEN bus_filing.cd_trans_type = 'LPC'   THEN 'Domestic Limited Partnership'
    WHEN bus_filing.cd_trans_type = 'STC'   THEN 'Domestic Statutory Trust'
    WHEN bus_filing.cd_trans_type = 'LCFC'  THEN 'Foreign Limited Liability Company'      
    WHEN bus_filing.cd_trans_type = 'CFWS'  THEN 'Foreign Stock Corporation'              
    WHEN bus_filing.cd_trans_type = 'CFWN'  THEN 'Foreign Non-Stock Corporation'          
    WHEN bus_filing.cd_trans_type = 'LLPFW' THEN 'Foreign Limited Liability Partnership'  
    WHEN bus_filing.cd_trans_type = 'LPFC'  THEN 'Foreign Limited Partnership'            
    WHEN bus_filing.cd_trans_type = 'STFC'  THEN 'Foreign Statutory Trust'    
    ELSE 'No' END AS ENTITY_TYPE, 
    bus_master.nm_name, 
    date_part('year', dt_effect) AS year_effect, 
    date_part('month', dt_effect) AS month_effect    
FROM bus_filing
JOIN bus_master ON bus_filing.id_bus = bus_master.id_bus
WHERE 
  cd_trans_type IN ('LCD', 'CDRS', 'CDRN', 'LLPR', 'LPC', 'STC', 'LCFC', 'CFWS', 'CFWN', 'LLPFW', 'LPFC', 'STFC') --dissolutions
ORDER BY 
  dt_effect DESC
"""

ADDRESS_CHANGE_QUERY = """
    SELECT
        id_bus_flng,
        EXTRACT(YEAR FROM dt_filing) AS year
    FROM
        bus_filing
    WHERE
        cd_trans_type IN ('ACM','LCACM','LCFACM','LLPACM','LLPFACM','LPACM','LPFACM','STACM','STFACM')
    """

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
    tx.company_type as type,
    CASE WHEN length(master.ad_city) > 0 then master.ad_city
     ELSE master.ad_mail_city
    END as city,
    CASE WHEN tx.stock = 'TRUE' then 'S'
     WHEN tx.nonstock = 'TRUE' then 'N'
     ELSE ''
    END as stock,
    CASE WHEN tx.domestic = 'TRUE' then 'D'
     WHEN tx.foreign_company = 'TRUE' then 'F'
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
    AND filing.dt_filing >= DATE('1980-01-01')
ORDER BY
    year ASC,
    month ASC,
    town ASC,
    cd_status ASC,
    cd_subtype ASC
"""

def extract_business_formations(conn, cursor, outfile, query):
    if query == 'Formations':
        outputquery = 'copy ({0}) to stdout with csv header'.format(EXTRACT_FORMATIONS_QUERY)
    elif query == 'Address':
        outputquery = 'copy ({0}) to stdout with csv header'.format(ADDRESS_CHANGE_QUERY)
    elif query == 'Starts':
        outputquery = 'copy ({0}) to stdout with csv header'.format(STARTS_QUERY)
    elif query == 'Stops':
        outputquery = 'copy ({0}) to stdout with csv header'.format(STOPS_QUERY)
    with open(outfile, 'w') as f:
        cursor.copy_expert(outputquery, f)






