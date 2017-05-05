from psycopg2 import connect

def connectDB(db, user, pwd, host, port):
    """Opens a psycopg2 db connction using configuration parems set in self.scriptVars."""
    conn = connect(database=db, user=user, password=pwd, host=host, port=port)
    cursor = conn.cursor()
    return conn, cursor