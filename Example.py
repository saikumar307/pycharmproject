import cx_Oracle

con = cx_Oracle.connect('SCOTT/tiger@orcl')
print("Connected successfully")
print("Oracle version :", con.version)
con.close()
