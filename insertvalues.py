# Write a python program to insert a row into a created employs table?

import cx_Oracle

try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    cur = con.cursor()
    cur.execute("INSERT INTO Employs VALUES(1001,'saikumar',18900,20)")
    con.commit()
    print('Row inserted successfully')
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
