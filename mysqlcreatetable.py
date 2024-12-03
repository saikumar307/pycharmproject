import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='saikumar', user='root', password='Saikumar@123')
    cur = con.cursor()
    cur.execute('CREATE TABLE Employs(EmpId INT(4), Ename VARCHAR(10), Salary FLOAT(8,2), DeptId INT(2))')
    print('Table created successfully')
except mysql.connector.DatabaseError as msg:
    print(msg)
finally:
    if cur:
        cur.close()
    if con:
        con.close()