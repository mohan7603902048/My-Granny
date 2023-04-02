#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
print('''<form action="signup.py" method="post">
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
<h1><b>SIGNUP PAGE</b></h1><br><br><br><br><br><br><br><br>
<h2>User name:<input type="text" name="uname"></h2>
<h2>Age:<input type="number" name="uage"></h2>
<h2>Phone number:<input type="number" name="uph"></h2>
<h2>Mail ID:<input type="Mail" name="umail"></h2>
<h2>Password:<input type="text" name="ups"></h2>
<h2>Re-enter password:<input type="text" name="ureps"></h2>
<b><input type="Submit" class="Submit" value="Signup" name="usignup"></b>
</center>
</body>
<style>
body{
        background-image:url("./image/img10.jpg");
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
     }
</style>
</form>

''')
