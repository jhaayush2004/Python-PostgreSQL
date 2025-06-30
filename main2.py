import psycopg2
from config import config

def connect():
    connection = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**params)

        #create a cursor
        crsr = connection.cursor()
        print("PostgreSQL database version: ")
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone() #we have fetchall() method also
        print(db_version)
        crsr.close()

    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally :
        if connection is not None:
            connection.close()
            print("Database Connection Terminated...")

if __name__ == "__main__":
  connect()


'''
Output:
(venv) D:\Documents\MLOps\Python-PostgreSQL>python main2.py
Connecting to the PostgreSQL database...
PostgreSQL database version: 
('PostgreSQL 17.5 on x86_64-windows, compiled by msvc-19.44.35209, 64-bit',)
Database Connection Terminated...
'''
