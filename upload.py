#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql
f=cgi.FieldStorage()
db=pymysql.Connect(host='localhost',user='root',password='mohan',database='mygranny')
cur=db.cursor()
#cur.execute("create table moha(Injuries_Illness varchar(100),symtomes varchar(100),homeremidies varchar(100),food varchar(100))")
Injuries_Illness=f.getvalue('health')
symtomes=f.getvalue('sym')
homeremidies=f.getvalue('horem')
food=f.getvalue('fd')
query="insert into moha values(%s,%s,%s,%s)"
val=[Injuries_Illness,symtomes,homeremidies,food]
cur.execute(query,val)
db.commit()
print('''<h1>uploaded sucessfully!!!</h1>''')
print('''
<center>
</form>
<form action="project1.html" method="post">
<br><br><br><br><br><br><br><br><center><h2 style="color:black;"><button style="font-family:Chiller script;color:white;padding:8px 45px;font-size:20px;background-color:blue" ;type="submit" class="button"><b>Logout</b></button></h2></center>
<style>
 body{
        background-image:url("./image/img2.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
</style>
</form>
''')

