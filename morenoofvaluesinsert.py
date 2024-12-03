# Write a python program to insert multiple rows into employs table?

import cx_Oracle

try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    cur = con.cursor()
    ins = "INSERT INTO Employs VALUES(:EmpId, :Ename, :Salary, :DeptId)"
    rows = [(1002, 'sai', 14500, 30), (1003, 'kumar', 23800, 20), (1004, 'chinta', 21000, 20)]
    cur.executemany(ins, rows)
    con.commit()
    print('Rows inserted successfully')
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
