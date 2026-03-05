import mysql.connector
def get_connection():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='programmer like me',
        port='3306',
        database='hms'
    )
    return mydb