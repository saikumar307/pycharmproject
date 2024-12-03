import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='saikumar', user='root', password='Saikumar@123')
    cur = con.cursor()
    cur.execute("INSERT INTO Employs VALUES(1001,'saikumar',18900,20)")
    con.commit()
except mysql.connector.DatabaseError as msg:
    print(msg)
finally:
    if cur:
        cur.close()
    if con:
        con.close()