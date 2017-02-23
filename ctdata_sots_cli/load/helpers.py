from sqlalchemy import create_engine

def setup_engine(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME):
    PG_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    engine = create_engine(PG_URI, echo=False)
    return engine
