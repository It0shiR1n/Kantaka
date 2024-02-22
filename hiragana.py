import re 

import mysql.connector
from mysql.connector import errorcode

def showHiragana(ideogram):
    romanji_pattern = re.compile("^[a-zA-Z0-9]+$")
    hiragana_pattern = re.compile(r'[\u3040-\u309F]+')  
    
    try:
        database = mysql.connector.connect(user='your-user', password='your-password', host='localhost', database='your-database')
        dbHandler = database.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            database.close()
            print("Something is wrong with your user name or password")
            exit(1)

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            database.close()
            print("Database does not exist")
            exit(1)

        else:
            database.close()
            print(err)
            exit(1)

    if romanji_pattern.match(ideogram):
        sql = f"SELECT * FROM tb_hiragana WHERE pronunciation = '{ideogram}'"
        
        dbHandler.execute(sql)
        queryResult = dbHandler.fetchall()

        if queryResult == []:
            database.close()
            return 1

        else:
            database.close()
            return queryResult[0]

    elif hiragana_pattern.match(ideogram):
        sql = f"SELECT * FROM tb_hiragana WHERE ideogram = '{ideogram[0]}'"
        
        dbHandler.execute(sql)
        queryResult = dbHandler.fetchall()

        if queryResult == []:
            database.close()
            return 1

        else:
            database.close()
            return queryResult[0]
