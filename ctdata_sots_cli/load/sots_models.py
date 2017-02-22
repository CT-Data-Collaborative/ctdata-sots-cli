from sqlalchemy import cast, text, Table, MetaData, Column, Integer, String, Float, Numeric, Date
from sqlalchemy import Time, TIMESTAMP, Boolean, ForeignKey, create_engine, select, func, and_, DDL, Index
from sqlalchemy.event import listen, listens_for
from sqlalchemy.orm import mapper, relationship, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement
import re


m_views = ['busmaster_mail_address_index', 'busmaster_name_index',
           'name_change_oldname_index', 'principal_name_index',
           'busmaster_place_of_business_address_index',
           'bus_id_index', 'filing_number_index']

table_mat_views = ['bus_other_join_table', 'corp_join_table', 'dom_llc_join_table', 'dom_llp_join_table',
                   'dom_limit_p_join_table', 'for_llc_join_table', 'for_lim_part_join_table',
                   'for_llp_join_table', 'for_stat_trust_join_table', 'gen_part_join_table']



Base = declarative_base(engine)


def create_engine(DB_USER, DB_PWD, DB_HOST):
    PG_URI = 'postgresql://{}:{}@{}:5432'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT)
    engine = create_engine(PG_URI, echo=True)
    return engine



def loadSession(Base, engine):
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


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
        con.execute("DROP TABLE IF EXISTS business_status;")
        con.execute("DROP TABLE IF EXISTS business_subtype;")
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


# Then we create a new table that includes a UUID lookup along with all of the selected elements from the temp_index
# Add index and then add foreign key relationship back to bus_master
#  For some reason, the compound query will not update correctly. Works fine in sql consle.
def _build_full_text_index_table(engine):
    with engine.connect() as con:
        con.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
        con.execute('DROP TABLE IF EXISTS full_text_index;')
        con.execute("CREATE TABLE full_text_index AS (SELECT uuid_generate_v4() as index_key, ti.primary_id, ti.id_bus, "
            "st.nm_name, st.type, sta.status, st.dt_origin, ti.table_name, ti.index_name, ti.search_type, "
            "st.address, st.street, st.city, st.state, st.zip, st.country, ti.document "
            "FROM temp_index "
            "AS ti "
            "JOIN (SELECT bm.id_bus, bm.nm_name, bm.dt_origin, "
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
            "ON ti.id_bus = sta.id_bus);")


# Finally we add in the index on the ts_vector column and indicate
def _build_table_indices(engine):
    with engine.connect() as con:
        con.execute('CREATE INDEX idx_ftx_search ON public.full_text_index USING gin (document);')
        con.execute('CREATE INDEX idx_ftx_date ON public.full_text_index USING btree(dt_origin);')
        con.execute('ALTER TABLE full_text_index ADD PRIMARY KEY (index_key);')

def _bus_filing_index(engine):
    with engine.connect() as con:
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
    _join_index_material_view(engine)
    _build_full_text_index_table(engine)
    _build_table_indices(engine)
    _bus_filing_index(engine)
    _final_cleanup(engine)


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


class BusinessStatus(Base):
    __tablename__ = 'business_status'
    cd_status = Column(String, primary_key=True)
    description = Column(String)


class BusinessSubtype(Base):
    __tablename__ = 'business_subtype'
    cd_subtype = Column(String, primary_key=True)
    description = Column(String)


class PrincipalNameIndex(Base):
    __table__ = create_mat_view(
        Base.metadata,
        "principal_name_index",
        select([
            Principal.primary_id, Principal.id_bus,
            cast('principal', String).label('table_name'),
            cast('principal_name', String).label('index_name'),
            cast('name', String).label('search_type'),
            func.to_tsvector(Principal.nm_name).label('document')
        ])
    )



# --------------------------------------------------------------------------------------
# Functions for building status and subtype tables
# --------------------------------------------------------------------------------------
#
def build_status_table(base, engine):
    status = [('AC', 'Active'), ('CN', 'Cancelled'), ('CS', 'Consolidation'), ('CV', 'Converted'), ('D', 'Dissolved'),
              ('DS', 'Unknown'), ('ER', 'Expired Reservation'), ('EX', 'Expired'), ('FF', 'Forfeited'), ('M', 'Merged'),
              ('RC', 'Reserved Cancel'), ('RD', 'Redomesticated'), ('RG', 'Registered'), ('RN', 'Renunciated'),
              ('RS', 'Reserved'), ('WD', 'Withdrawn'), ('RV', 'Revoked'), ('W', 'W Second'), ('RE', 'Recorded'),
              ('PM', 'Pending Merger'), ('PC', 'Pending Conversion'), ('CO', 'Converted Out')]
    session = loadSession(base, engine)
    session.add_all([BusinessStatus(cd_status=x[0], description=x[1]) for x in status])
    session.commit()


def build_subtype_table(base, engine):
    types = [('C', 'Corporation'), ('D', 'Domestic Limited Partnership'), ('F', 'Foreign Limited Partnership'),
             ('G', 'Domestic Limited Liability Company'), ('H', 'Foreign Limited Liability Company'),
             ('I', 'Domestic Limited Liability Partnership'), ('J', 'Foreign Limited Liability Partnership'),
             ('K', 'General Partnership'), ('L', 'Domestic Statutory Trust'), ('M', 'Foreign Statutory Trust'),
             ('O', 'Other'), (' ', 'Unknown'), ('P', 'Domestic Stock Corporation'), ('Q', 'Foreign Stock Corporation'),
             ('R', 'Domestic Non-Stock Corporation'), ('S', 'Foreign Non-Stock Corporation'), ('T', 'All Entities'),
             ('U', 'Domestic Credit Union Stock'), ('V', 'Domestic Credit Union Non-Stock'),
             ('W', 'Domestic Bank Stock'), ('X', 'Domestic Bank Non-Stock'), ('Y', 'Domestic Insurance Stock'),
             ('Z', 'Domestic Insurance Non-Stock'), ('B', 'Benefit Corporation')]
    session = loadSession(base, engine)
    session.add_all([BusinessSubtype(cd_subtype=x[0], description=x[1]) for x in types])
    session.commit()
