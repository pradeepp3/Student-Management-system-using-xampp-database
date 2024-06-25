import mysql.connector
con_o=mysql.connector.connect(host="localhost",user="root",password="",database="sam")
cur_o=con_o.cursor()

#code for deleting all the rows to get a new table in the database
'''truncate_query = "TRUNCATE TABLE studentman"
cur_o.execute(truncate_query)
con_o.commit()
#end
'''
###actual code (querying)
a=input("Name: ")
b=input("Register No: ")
c=int(input("Age: "))
d=float(input('Attendence: '))
e=input("Course Name: ")
f=float(input("CGPA: "))
g=input("Gender: ")
#insert code
q2="INSERT INTO `studentman`(`Name`, `Register No`, `Age`, `Attendence`, `Course Name`, `CGPA`, `Gender`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cur_o.execute(q2,(a, b, c, d, e, f, g))
con_o.commit()
##ending steps
cur_o.close()
con_o.close()