import os
import pymysql

# Get username
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # close connection, regardless of whether the above was successful
    connection.close()
