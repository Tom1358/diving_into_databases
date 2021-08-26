import os
import datetime
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
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    # close connection, regardless of whether the above was successful
    connection.close()
