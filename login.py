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
        print('''<form action="search.py" method="post">
        <title>SEARCH</title>
        <body>
        <center>
        <style>
        h1 {padding-top:50px;
            padding-bottom:10px;
            }
        .submit{font-size:20px;
                padding:10px;
                border-radius:100px;
                margin:50px;
                print;colour:white; 
                }
        </style>
        <h1><b>Search the Remedies</b></h1><br><br><br><br><br>
        <h2>Injuries/Illness:<input type="text" name="uinjuri" size=90px></h2><br><br><br>
        <b><input type="Submit" class="Submit" value="SEARCH" name="usearch"></b>
        </center>
        </body>
        <style>
        body{
        background-image:url("./image/img3.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
        }
        </style>
        </form>

        ''')
            
