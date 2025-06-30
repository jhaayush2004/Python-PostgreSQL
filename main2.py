import psycopg2
from config import config

def connect():
    connection = None
    try:
        params = config()
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**params)

        #create a cursor
        # This line creates a cursor object from the active database connection.
        # 'crsr' is now your interface to interact with the database.
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

'''
# Key Roles of a Cursor:
Executing SQL Queries: It's the primary object you use to send SQL statements (like SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, etc.) to the database server.

Fetching Results: After executing a SELECT query, the results (the rows returned by the database) are buffered by the cursor. You then use methods on the cursor (like fetchone(), fetchall(), fetchmany()) to retrieve these results into your Python program.

Managing Database State (within a connection): A single database connection (connection in your code) can have multiple cursors open simultaneously. Each cursor maintains its own state, including the results of its last query. This allows you to work with different query results independently on the same connection.
'''