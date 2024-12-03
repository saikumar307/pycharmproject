import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='saikumar', user='root', password='Saikumar@123')
    cur = con.cursor()
    cur.execute("SELECT * FROM sai")
    row = cur.fetchone()  #
    while True:
        if row is None:
            break
        print(row)
        row = cur.fetchone()
except mysql.connector.DatabaseError as msg:
    print(msg)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
