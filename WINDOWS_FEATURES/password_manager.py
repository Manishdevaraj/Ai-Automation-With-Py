import random
import mysql.connector


lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="`~!@#$%^&*()_-=+[]:;'""/?.,><|"
string=lower+upper+number+symbol
length=8
password1="".join(random.sample(string,length))
print(password1)

mydb= mysql.connector.connect(host='localhost', user='root', password='blacky062005',auth_plugin='mysql_native_password')
mycur=mydb.cursor()
mycur.execute("USE PASSWORD_MANAGER")
USERNAME="MANISH"
PLATFORM="FACEBOOK"
PASSWORD=password1
sql = "INSERT INTO USERNAME_PASSWORD (USERNAME, PLATFORM, P_ASSWORD) VALUES (%s, %s, %s)"
values = (USERNAME, PLATFORM, PASSWORD)
mycur.execute(sql,values)


mydb.commit()