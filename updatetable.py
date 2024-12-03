import cx_Oracle

try:
    con = cx_Oracle.connect("Scott/tiger@orcl")
    cur = con.cursor()
    incr = float(input("Enter increment salary percentage : "))
    updqry = "UPDATE Employs SET SALARY = SALARY + SALARY * %f / 100"
    cur.execute(updqry % (incr))
    con.commit()
    print("Rows updated successfully")
except cx_Oracle.DatabaseError as msg:
    print(msg)
finally:
    if cur:
        cur.close()
    if con:
        con.close()
