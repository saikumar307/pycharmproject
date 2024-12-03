# Write a python program to drop employs table from Oracle database?

import cx_Oracle

try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    cur = con.cursor()
    cur.execute('Drop Table Employs')
    print('Table dropped successfully')
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
