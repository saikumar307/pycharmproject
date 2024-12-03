#Write a python program to retrieve all rows from Employs table?


import cx_Oracle
try:
    con=cx_Oracle.connect('SCOTT/tiger@orcl')
    cur=con.cursor()
    cur.execute("SELECT * FROM Employs")
    rows=cur.fetchall()
    for row in rows:
        print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])
except cx_Oracle.DatabaseError as e:
    print(e)
    if cur:
        cur.close()
    if con:
        con.close()