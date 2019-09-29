import  psycopg2
from config_db import  config

def connect():
    """
    Connect to the PostgreSQL database server
    """
    try:
        params = config()
        print("Connecting to the PostgreSQL database..")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('database version:')
        cur.execute('SELECT vesion()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")
