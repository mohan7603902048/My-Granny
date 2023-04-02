#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
f=cgi.FieldStorage()
db=pymysql.Connect(host='localhost',user='root',password='mohan',database='mygranny')
cur=db.cursor()
Username=f.getvalue('uname')
Age=f.getvalue('uage')
Phonenumber=f.getvalue('number')
Mail=f.getvalue('umail')
Password=f.getvalue('ups')
Repassword=f.getvalue('ureps')
if Password==Repassword:
    query="insert into menu values(%s,%s,%s,%s,%s,%s)"
    val=[Username,Age,Phonenumber,Mail,Password,Repassword]
    cur.execute(query,val)
    db.commit()
    print('''<form action="uploader.py" method="post">
        <title>SIGNUP</title>
        <body>
        <center>
        <style>
        h2{
            color:tomato;
        }
        h1{
            color:green;
        }
        .LOGIN{width:100px; heigt:50px; font-size:20px; background:blue; color:white;}
        </style>
        <h1><b>LOGIN PAGE</b></h1><br><br>
        <h2>Mail ID:<input type="text" name="umail"</h2>
        <h2>Password:<input type="text" name="upass"</h2><br><br>
        <b><input type="Submit" class="LOGIN" value="login"></b>
        </center>
        </body>
        <style>
        body{
               background-image:url("./image/img1.jpg");
               background-repeat:no-repeat;
               background-size:cover;
               background-attachment:fixed;
        }
        </style>
        </form>
        
        ''')
else:
    print('''<form action="adminsignup.py" method="post">
    <title>SIGNUP</title>
    <body>
    <center>
    <style>
    h1 {padding-top:50px;
        padding-bottom:10px;
        }
    .submit{font-size:40px;
            padding:10px;
            border-radius:100px;
            margin:50px;
            print;colour:white; 
            }
    </style>
    <h1><b>SIGNUP PAGE</b></h1><br><br>
    <h2>User name:<input type="text" name="uname"></h2>
    <h2>Age:<input type="number" name="uage"></h2>
    <h2>Phone number:<input type="number" name="uph"></h2>
    <h2>Mail ID:<input type="Mail" name="umail"></h2>
    <h2>Password:<input type="text" name="ups"></h2>
    <h2>Re-enter password:<input type="text" name="ureps"></h2><br><br><br>
    <b><input type="Submit" class="Submit" value="Signup" name="usignup"></b>
    </center>
    </body>
    <style>
     body{
        background-image:url("13.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
    </style>
    </form>
    ''')







  
