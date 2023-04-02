#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
f=cgi.FieldStorage()

name=f.getvalue("name")
age=f.getvalue("age")
email=f.getvalue("mail")
psw1=f.getvalue("psw")
re_psw1=f.getvalue("re_psw")

if psw1==re_psw1:
    print('''
    <form action="signup.py" method="post">
    <hr></hr>
    <img src="one.jpg" img align="right" width="300" height="90">
    <h1 style="font-times new roman;color:orange;padding-left:620px;font-size:40px"><b><u> MY GRANNY</u></b></h1>
    <hr></hr>
    <center><h2><label style="font-times new roman;color:green;font-size:35px"><u>WELCOME TO THIS PAGE</u></h2></center>
    </form>
    <style>
    button
    {
        font-size:40px;
        padding:10px;
        border-radius:100px;
        margin:50px;
        print;colour:white;
        background:linear-gradient(to right,#50C878,#3EB489);
    }
    </style>
    <html>
    <body>
    <center><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <button id="uploader">UPLOADER</button>
    <button id="user">USER</button>
    </center>
    <style>
    body{
        background-image:url("3.1.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
    </style>
    </center>
    </form>
    </body>
    ''')

else:
    print('''
    <form action="login.py" method="post">
    <hr></hr>
    <img src="0ne.jpg" img align="right" width="300" height="90">
    <h1 style="font-times new roman;color:orange;padding-left:620px;font-size:40px"><b><u> MY GRANNY</u></b></h1>
    <hr></hr>
    <center><h2><label style="font-times new roman;color:green;font-size:35px"><u>WELCOME TO THIS PAGE</u></h2></center>
    </form>
    <style>
    button
    {
        font-size:40px;
        padding:10px;
        border-radius:100px;
        margin:50px;
        print;colour:white;
        background:linear-gradient(to right,#50C878,#3EB489);
    }
    </style>
    <html>
    <body>
    <center><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <button id="uploader">UPLOADER</button>
    <button id="user">USER</button>
    </center>
    <style>
    body{
        background-image:url("3.1.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
    </style>
    </center>
    </form>
    </body>
   
    ''')







