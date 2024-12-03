# Write a python program to input deptid and delete the
# rows from Employs table based on that DeptId?

import cx_Oracle
from cx_Oracle import DatabaseError

try:
    con=cx_Oracle.connect('SCOTT/tiger@orcl')
    cur=con.cursor()
    did=int(input("enter id :"))
    delqry="DELETE FROM Employs WHERE DeptId=%d"
    cur.execute(delqry % (did))
    con.commit()
except cx_Oracle.DatabaseError as e:
    print(e)
    if cur:
        cur.close()
    if con:
        con.close()
