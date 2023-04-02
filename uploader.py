#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql
f=cgi.FieldStorage()
db=pymysql.Connect(host='localhost',user='root',password='mohan',database='mygranny')
cur=db.cursor()
email=f.getvalue('umail')
password=f.getvalue('upass')
cur.execute("select * from menu")

for i in cur:
    if email==i[3] and password==i[4]:
        print('''<form action="upload.py" method="post">
        <head>
        <center> 
        <style>
        p {font-size:25px;font-family:times new roman}
        .side{
            margin-left:30%;
            margin-top:2%;
        }
        </style>
        <h1><br><br><br>
          <div class="side">
        <h1>WHAT TYPE OF INJURIS  ILLNESS UPLOAD HERE</h1><br>
        </head>
      
        <b><p>Upload Injuries/Illness :<input type="text" name="health"></p></b>
        <b><p>symtomes:<input type="text" name="sym"></p></b>
        <b><p>homeremidies:<input type="text" name="horem"></p></b>
        <b><p>food:<input type="text" name="fd"></p></b>
        <button><type="Submit" class="button"><b>UPLOAD</b></button>
        </div>
        </center>
        </form>

        <style>
        body{
                background-image:url("./image/img9.jpg");
                background-repeat:no-repeat;
                background-size:cover;
                background-attachment:fixed;
             }
        </style> 
         ''')

            
