import re
from sqlalchemy import cast, Table, MetaData, Column, String, select, func, DDL
from sqlalchemy.event import listen, listens_for
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement
#from sqlalchemy.sql.expression import ColumnElement, _literal_as_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from lib import project_config
import click
# from sqlalchemy import cast, text, Table, MetaData, Column, Integer, String, Float, Numeric, Date
# from sqlalchemy import Time, TIMESTAMP, Boolean, ForeignKey, select, func, and_, DDL, Index
# from sqlalchemy.orm import mapper, relationship, sessionmaker, Session

m_views = ['busmaster_mail_address_index', 
           'busmaster_name_index',
           'name_change_oldname_index', 
           'principal_name_index',
           'agent_name_index',
           'busmaster_place_of_business_address_index',
           'busmaster_place_of_business_city_index',
           'bus_id_index', 
           'filing_number_index']

table_mat_views = ['bus_other_join_table', 
                   'corp_join_table', 
                   'dom_llc_join_table', 
                   'dom_llp_join_table',
                   'dom_limit_p_join_table', 
                   'for_llc_join_table', 
                   'for_lim_part_join_table',
                   'for_llp_join_table', 
                   'for_stat_trust_join_table', 
                   'gen_part_join_table']


# def loadSession(Base, engine):
#     """"""
#     metadata = Base.metadata
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session


# --------------------------------------------------------------------------------------
# Housekeeping functions for dropping tables and views
# --------------------------------------------------------------------------------------
# Cleanup - Drop Materialized Views
def cleanup_index_mat_view(engine):
    with engine.connect() as con:
        for view in m_views:
            dropstring = 'DROP MATERIALIZED VIEW IF EXISTS {}'.format(view)
            try:
                con.execute(dropstring)
            except:
                pass


# Cleanup - Drop Full Text Index Table
def cleanup_index_tables(engine):
    with engine.connect() as con:
        con.execute("DROP TABLE IF EXISTS full_text_index;")
        con.execute("DROP TABLE IF EXISTS temp_index;")


# Drop views depending on config setting
def cleanup_table_mat_views(engine):
    with engine.connect() as con:
        for view in table_mat_views:
            dropstring = 'DROP MATERIALIZED VIEW IF EXISTS {}'.format(view)
            try:
                con.execute(dropstring)
            except:
                pass


# --------------------------------------------------------------------------------------
# Helper functions for building materialized views
# --------------------------------------------------------------------------------------

# Helper function for translating class names to table names
def camel_to_underscore(name):
    """coerce camelcase to lowercase with underscore separation"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# Helpers for generating materialized views
class CreateMaterializedView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


@compiler.compiles(CreateMaterializedView)
def compile(element, compiler, **kw):
    # Could use "CREATE OR REPLACE MATERIALIZED VIEW..."
    # but I'd rather have noisy errors
    return "CREATE MATERIALIZED VIEW %s AS %s" % (
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


def create_mat_view(metadata, name, selectable):
    _mt = MetaData()  # temp metadata just for initial Table object creation
    t = Table(name, _mt)  # the actual mat view class is bound to db.metadata
    for c in selectable.c:
        t.append_column(Column(c.name, c.type, primary_key=c.primary_key))

    listen(
        metadata, "after_create",
        CreateMaterializedView(name, selectable)
    )

    @listens_for(metadata, "after_create")
    def create_indexes(target, connection, **kw):
        for idx in t.indexes:
            idx.create(connection)

    listen(
        metadata, "before_drop",
        DDL('DROP MATERIALIZED VIEW IF EXISTS ' + name)
    )
    return t

def join_supplemental_tables(engine):
    failed = []
    with engine.connect() as con:
        con.execute('DROP TABLE IF EXISTS bus_master_sup')
        con.execute('CREATE TABLE bus_master_sup AS (SELECT * from {});'.format(table_mat_views[0]))
        for v in table_mat_views[1:]:
            try:
                con.execute('INSERT INTO bus_master_sup (SELECT * from {})'.format(v))
            except:
                failed.append(v)
    print(failed)
    return failed


# --------------------------------------------------------------------------------------
# Main functions for full_text_index
# --------------------------------------------------------------------------------------

# First we join the materialized views into temp_index
def _join_index_material_view(engine):
    failed = []
    with engine.connect() as con:
        con.execute('DROP TABLE IF EXISTS temp_index')
        con.execute('CREATE TABLE temp_index AS (SELECT * from {});'.format(m_views[0]))
        for v in m_views[1:]:
            try:
                con.execute('INSERT INTO temp_index (SELECT * from {})'.format(v))
            except:
                failed.append(v)
    print(failed)
    return failed

def _build_supp_tables(engine):
    with engine.connect() as con:
        #principalname        
        con.execute('DROP TABLE IF EXISTS principalname;')
        con.execute("CREATE TABLE principalname as (SELECT primary_id, q2.id_bus, principal_name "
            "FROM ( "
                "SELECT id_bus, string_agg(nm_name, ', ') AS principal_name FROM "
                    "(SELECT DISTINCT id_bus, nm_name, "
                    "ROW_NUMBER() OVER(PARTITION BY id_bus, nm_name ORDER BY id_bus) as name_index " #some principals are principals for more than one business
                    "FROM principal "
                    "ORDER BY id_bus) as q1 "
                "WHERE q1.name_index = 1 "
                "GROUP BY id_bus "
            ") as q2 "
            "LEFT JOIN ( "
                "SELECT primary_id, id_bus FROM ( "
                    "SELECT primary_id, id_bus, "
                    "ROW_NUMBER() OVER(PARTITION BY id_bus ORDER BY primary_id) as id_index FROM principal "
                ") as q3 "
                "WHERE q3.id_index = 1 "
            ") as q4 "
            "on q2.id_bus = q4.id_bus);")
        con.execute("ALTER TABLE principalname ADD PRIMARY KEY (primary_id);")
        #filing date
        con.execute('DROP TABLE IF EXISTS filingdate;')
        con.execute("CREATE TABLE filingdate as (SELECT id_bus, dt_filing, to_char(dt_filing, 'MM/dd/yyyy') as dt_filing2 "
            "FROM bus_filing "
            "JOIN tx_codes "
            "on bus_filing.cd_trans_type = tx_codes.cd_trans_type "  
            "WHERE tx_codes.label ilike '%%formation%%' "
            "ORDER BY id_bus, dt_filing);")        
        #filing details
        con.execute("DROP TABLE IF EXISTS filingdetails;")
        con.execute("CREATE TABLE filingdetails as ( "
            "SELECT DISTINCT ROW_NUMBER() OVER(ORDER BY dt_filing) as id_index,  "
            "id_bus, dt_filing, to_char(dt_filing, 'MM/dd/yyyy') as dt_filing2, bus_filing.id_bus_flng, tx_certif, "
            "coalesce(volume_type, 'No data') as volume_type, "
            "coalesce(volume_number, 'No data') as volume_number, "
            "coalesce(start_page, 'No data') as start_page, "
            "coalesce(pages, 'No data') as pages "
            "FROM bus_filing "
            "INNER JOIN ( "
            "SELECT DISTINCT id_bus_flng, volume_type, volume_number, start_page, pages "
            "FROM filmindx) as sq1 "
            "ON bus_filing.id_bus_flng = sq1.id_bus_flng);")
        con.execute("ALTER TABLE filingdetails ADD PRIMARY KEY (id_index);")
    
def _alter_tables(engine):
    with engine.connect() as con:
        con.execute("ALTER TABLE bus_filing ADD dt_filing2 text;")
        con.execute("UPDATE bus_filing SET dt_filing2 = to_char(dt_filing, 'MM/dd/YYYY');")

# Then we create a new table that includes a UUID lookup along with all of the selected elements from the temp_index
# Add index and then add foreign key relationship back to bus_master
#  For some reason, the compound query will not update correctly. Works fine in sql consle.
def _build_full_text_index_table(engine):
    with engine.connect() as con:
        con.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
        con.execute('DROP TABLE IF EXISTS full_text_index;')
        con.execute("CREATE TABLE full_text_index AS (SELECT uuid_generate_v4() as index_key, ti.primary_id, ti.id_bus, "
            "st.nm_name, st.type, sta.status, st.dt_origin, ti.table_name, ti.index_name, ti.search_type, "
            "st.address, st.street, st.city, st.state, st.zip, st.country, ti.document, "
            #adding principal name and agent name to table
            "prin.principal_name, st.nm_agt ,  "
            #adding filing date 
            "fl.dt_filing, fl.dt_filing2 "
            "FROM temp_index "
            "AS ti "
            "JOIN (SELECT bm.id_bus, bm.nm_name, bm.dt_origin, bm.nm_agt, "
            "CASE "
            "WHEN (bm.ad_city is not NULL) THEN concat_ws(' ', concat_ws(', ', bm.ad_str1, bm.ad_str2, bm.ad_str3, bm.ad_city, bm.ad_st), ad_zip5, bm.ad_cntry) "
            "ELSE concat_ws(' ', concat_ws(', ', bm.ad_mail_str1, bm.ad_mail_str2, bm.ad_mail_str3, bm.ad_mail_city, bm.ad_mail_st), bm.ad_mail_zip5, bm.ad_mail_cntry) "
            "END AS address, "
            "CASE WHEN (bm.ad_city is not NULL) "
                    "THEN concat_ws(', ', bm.ad_str1, bm.ad_str2, bm.ad_str3) "
                    "ELSE concat_ws(', ', bm.ad_mail_str1, bm.ad_mail_str2, bm.ad_mail_str3) END AS street, "
            "CASE WHEN (bm.ad_city is not NULL) THEN bm.ad_city ELSE bm.ad_mail_city END AS city, "
            "CASE WHEN (bm.ad_city is not NULL) THEN bm.ad_zip5 ELSE bm.ad_mail_zip5 END AS zip, "
            "CASE WHEN (bm.ad_city is not NULL) THEN bm.ad_st ELSE bm.ad_mail_st END AS state, "
            "CASE WHEN (bm.ad_city is not NULL) THEN bm.ad_cntry ELSE bm.ad_mail_cntry END AS country, "
            "bs.description "
            "AS type "
            "FROM bus_master "
            "AS bm "
            "JOIN business_subtype "
            "AS bs "
            "ON bm.cd_subtype = bs.cd_subtype) "
            "AS st "
            "ON ti.id_bus = st.id_bus "
            "JOIN (SELECT bm.id_bus, bstatus.description "
            "AS status "
            "FROM bus_master "
            "AS bm "
            "JOIN business_status "
            "AS bstatus "
            "ON bm.cd_status = bstatus.cd_status) "
            "AS sta "
            "ON ti.id_bus = sta.id_bus "
            #adding principal name to table
            "LEFT JOIN (SELECT DISTINCT id_bus, principal_name FROM principalname " #not all business have principals (left join), select distinct principals (no multiple titles)
            "GROUP BY id_bus, principal_name) "
            "AS prin "
            "ON ti.id_bus = prin.id_bus "
            #adding filing date to table
            "LEFT JOIN (SELECT id_bus, dt_filing, dt_filing2 FROM filingdate) "
            "AS fl "
            "ON ti.id_bus = fl.id_bus "
            ");")
        
# Finally we add in the index on the ts_vector column and indicate
def _build_table_indices(engine):
    with engine.connect() as con:
        con.execute('CREATE INDEX idx_ftx_search ON public.full_text_index USING gin (document);')
        con.execute('CREATE INDEX idx_ftx_date ON public.full_text_index USING btree(dt_origin);')
        con.execute('ALTER TABLE full_text_index ADD PRIMARY KEY (index_key);')

def _bus_filing_index(engine):
    with engine.connect() as con:
        con.execute('DROP INDEX IF EXISTS filing_index;')
        con.execute('CREATE INDEX filing_index ON public.bus_filing USING btree(id_bus, cd_trans_type);')

def _final_cleanup(engine):
    with engine.connect() as con:
        for view in m_views:
            dropstring = 'DROP MATERIALIZED VIEW IF EXISTS {};'.format(view)
            try:
                rs = con.execute(dropstring)
            except:
                pass
        con.execute('DROP TABLE IF EXISTS temp_index;')


def build_index(engine):
    Base = declarative_base(engine)

    class SOTSMixin(object):
        @declared_attr
        def __tablename__(cls):
            return camel_to_underscore(cls.__name__)

        __table_args__ = {'autoload': True}

    class BusMaster(SOTSMixin, Base):
        pass

    class BusFiling(SOTSMixin, Base):
        pass

    class BusOther(SOTSMixin, Base):
        pass

    class Principal(SOTSMixin, Base):
        pass

    class GenPart(SOTSMixin, Base):
        pass

    class NameChange(SOTSMixin, Base):
        pass

    class Corp(SOTSMixin, Base):
        pass

    class DomLmtCmpy(SOTSMixin, Base):
        pass

    class DomLmtLiabPart(SOTSMixin, Base):
        pass

    class DomLmtPart(SOTSMixin, Base):
        pass

    class ForLmtCmpy(SOTSMixin, Base):
        pass

    class ForLmtLiabPart(SOTSMixin, Base):
        pass

    class ForLmtPart(SOTSMixin, Base):
        pass

    class ForStatTrust(SOTSMixin, Base):
        pass

    # --------------------------------------------------------------------------------------
    # Business Status
    # --------------------------------------------------------------------------------------
    class BusinessStatus(Base):
        __tablename__ = 'business_status'
        cd_status = Column(String, primary_key=True)
        description = Column(String)

    # --------------------------------------------------------------------------------------
    # Business Subtype
    # --------------------------------------------------------------------------------------
    class BusinessSubtype(Base):
        __tablename__ = 'business_subtype'
        cd_subtype = Column(String, primary_key=True)
        description = Column(String)

    # --------------------------------------------------------------------------------------
    # Principal Name
    # --------------------------------------------------------------------------------------

    class PrincipalNameIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            "principal_name_index",
           select([
               Principal.primary_id, Principal.id_bus, 
               cast('principal', String).label('table_name'),
               cast('principal_name', String).label('index_name'),
               cast('principal_name', String).label('search_type'),
               func.to_tsvector(Principal.nm_name).label('document')
           ])          
        )
        
    # --------------------------------------------------------------------------------------
    # Agent Name
    # --------------------------------------------------------------------------------------
    class AgentNameIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            "agent_name_index",
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('agent_name', String).label('index_name'),
                cast('agent_name', String).label('search_type'),
                func.to_tsvector(BusMaster.nm_agt).label('document')
            ])
        )
    # --------------------------------------------------------------------------------------
    # Business Mailing Address
    # --------------------------------------------------------------------------------------
    class BusMasterMailAddressIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'busmaster_mail_address_index',
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('business_mail_address', String).label('index_name'),
                cast('address', String).label('search_type'),
                func.to_tsvector(
                    func.CONCAT_WS(' ', BusMaster.ad_mail_str1, BusMaster.ad_mail_str2, BusMaster.ad_mail_str3,
                                   BusMaster.ad_mail_city, BusMaster.ad_mail_st,
                                   BusMaster.ad_mail_zip5, BusMaster.ad_mail_cntry)).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Place of Business Address
    # --------------------------------------------------------------------------------------
    class BusMasterPlaceaOfBusinessAddressIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'busmaster_place_of_business_address_index',
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('place_of_business_address', String).label('index_name'),
                cast('address', String).label('search_type'),
                func.to_tsvector(func.CONCAT_WS(' ', BusMaster.ad_str1, BusMaster.ad_str2, BusMaster.ad_str3,
                                                BusMaster.ad_city, BusMaster.ad_st,
                                                BusMaster.ad_zip5, BusMaster.ad_cntry)).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Place of Business City
    # --------------------------------------------------------------------------------------
    class BusMasterPlaceaOfBusinessCityIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'busmaster_place_of_business_city_index',
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('place_of_business_city', String).label('index_name'),
                cast('city', String).label('search_type'),
                func.to_tsvector(BusMaster.ad_city).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Business Name
    # --------------------------------------------------------------------------------------
    class BusMasterNameIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'busmaster_name_index',
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('business_name', String).label('index_name'),
                cast('name', String).label('search_type'),
                func.to_tsvector(BusMaster.nm_name).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Old Business Name
    # --------------------------------------------------------------------------------------
    class NameChangeOldNameIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'name_change_oldname_index',
            select([
                NameChange.primary_id, NameChange.id_bus,
                cast('name_change', String).label('table_name'),
                cast('name_change_oldname', String).label('index_name'),
                cast('name', String).label('search_type'),
                func.to_tsvector(NameChange.nm_old).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Business Filing Number
    # --------------------------------------------------------------------------------------
    class FilingNumberIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'filing_number_index',
            select([
                BusFiling.primary_id, BusFiling.id_bus,
                cast('bus_filing', String).label('table_name'),
                cast('filing_number', String).label('index_name'),
                cast('filing_number', String).label('search_type'),
                func.to_tsvector(BusFiling.id_bus_flng).label('document')
            ])
        )

    # --------------------------------------------------------------------------------------
    # Business ID
    # --------------------------------------------------------------------------------------
    class BusIDIndex(Base):
        __table__ = create_mat_view(
            Base.metadata,
            'bus_id_index',
            select([
                BusMaster.primary_id, BusMaster.id_bus,
                cast('bus_master', String).label('table_name'),
                cast('bus_id', String).label('index_name'),
                cast('bus_id', String).label('search_type'),
                func.to_tsvector(BusMaster.id_bus).label('document')
            ])
        )
        
    click.echo("Prep cleanup")
    cleanup_table_mat_views(engine)
    cleanup_index_tables(engine)
    cleanup_index_mat_view(engine)

    click.echo("Creating declared models")
    Base.metadata.create_all(engine)
    
    click.echo("Building Supplemental Tables")
    _build_supp_tables(engine)

    click.echo("Joining Material Views")
    _join_index_material_view(engine)
    
    click.echo("Altering Tables")
    _alter_tables(engine)
    
    click.echo("Building Full Text Index")
    _build_full_text_index_table(engine)

    click.echo("Adding table column indices")
    _build_table_indices(engine)
    _bus_filing_index(engine)

    click.echo("Cleaning up")
    _final_cleanup(engine)


