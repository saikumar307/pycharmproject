#Write a python program to retrieve one row at a time from Employs table?

import cx_Oracle

try:
    con = cx_Oracle.connect("Scott/tiger@orcl")
    cur = con.cursor()
    cur.execute("SELECT * FROM Employs")
    row = cur.fetchone()	#
    while True:
        if row is None:
            break
        print(row)
        row = cur.fetchone()
except cx_Oracle.DatabaseError as msg:
    print(msg)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
