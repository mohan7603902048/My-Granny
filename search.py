#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql
f=cgi.FieldStorage()
db=pymysql.Connect(host='localhost',user='root',password='mohan',database='mygranny')
cur=db.cursor()
r=f.getvalue("uinjuri")
query="select * from moha"
cur.execute(query)
for i in cur:
    if i[0]==r:
        print("<h1 style=font-family:Arial print;>Injuries/Illness;",i[0],"</h1>")
        print("<h1 style=font-family:Arial print;>symptoms;",i[1],"</h1>")
        print("<h1 style=font-family:Arial print;>homeremedies;",i[2],"</h1>")
        print("<h1 style=font-family:Arial print;>food;",i[3],"</h1>")
print('''
<center>
</form>
<form action="project1.html" method="post">
<br><br><br><br><br><br><br><br><center><h2 style="color:yellow;"><button style="font-family:Chiller script;color:white;padding:8px 45px;font-size:20px;background-color:blue" ;type="submit" class="button"><b>Logout</b></button></h2></center>
<style>
body{
        background-image:url("./image/img8.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
</style>
</form>
''')


        
        
