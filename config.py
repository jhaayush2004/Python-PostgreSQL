from configparser import ConfigParser


def config(filename = "database.ini", section = "postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {} # empty dictionary 
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception(
            'Section{0} is not found in the {1} file.'.format(section,filename)
        )
    
  
    return db

if __name__ == "__main__" :
    config()

'''
Output: when print(db) added to code
(venv) D:\Documents\MLOps\Python-PostgreSQL>python config.py
{'host': 'localhost', 'database': 'master', 'user': 'postgres', 'password': '1234'}
'''