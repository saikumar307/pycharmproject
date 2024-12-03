# Write a python program to insert one row at a time
# for multiple rows with dynamic input until choice by user is no?



import cx_Oracle

try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    cur = con.cursor()
    while True:
        Empid = int(input("Enter EmpId : "))
        Ename = input("Enter Ename : ")
        Salary = float(input("Enter Salary : "))
        Deptid = int(input("Enter DeptId : "))
        ins = "INSERT INTO Employs VALUES(%d, '%s', %f, %s)"
        cur.execute(ins % (Empid,Ename,Salary,Deptid))
        print("Row inserted successfully")
        ch = input("Do u want to store another row : ")
        if ch == "No":
            con.commit()
            break
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    if cur:
        cur.close()
    if con:
        con.close()

