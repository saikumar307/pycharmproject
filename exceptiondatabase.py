import cx_Oracle
try:
    con = cx_Oracle.connect('SCOTT/tiger@orcl')
    print("Connected successfully")
    print("Oracle version :", con.version)
    con.close()
except cx_Oracle.DatabaseError as e:
    print(e)