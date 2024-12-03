import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='saikumar', user='root', password='Saikumar@123')
    if con.is_connected():
        print("Connected successfully")
        dbinfo = con.get_server_info()
        print(dbinfo)
except mysql.connector.DatabaseError as msg:
    print(msg)
finally:
    if con:
        con.close()