# Write a python program to create a employs table
# with columns empid, ename, salary and deptid in Oracle database?


import cx_Oracle

try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    cur = con.cursor()
    cur.execute('Create Table Employs (EmpId NUMBER(4), Ename VARCHAR2(10), Salary NUMBER(8,2), DeptId NUMBER(2))')
    print('Table created successfully')
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
