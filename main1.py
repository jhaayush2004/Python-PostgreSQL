'connection postgreSQL to Python'
import psycopg2
#connect(): creates new database session
connection = psycopg2.connect(host = "locahost",port = "5432", 
             database = "master", user = "postgres", password = "1234" )

'This is not efficient method of connection so will do another method using main2.py and database.ini'
'''An INI file is configuration file consisting of text based content with structure and 
syntax comprising key value pair for properties, and sections that organize the properties'''

"""
We chose this method bcoz by using database.ini, we can change the postgresql connection parameters
when we move the code to production environment without modifying the code.
so, in time of deployent, we don't have to change everytime inside the code instead
we will just make our modification separately inside our database.ini file.
"""