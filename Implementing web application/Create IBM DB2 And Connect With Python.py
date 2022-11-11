import ibm_db
dictionary={}
def printTableData(conn):
sql = "SELECT * FROM userdetails"
out = ibm_db.exec_immediate(conn, sql)
document = ibm_db.fetch_assoc(out)
while document != False:
dictionary.update({document['USERNAME']:
documen t['PASSWORD']})
document = ibm_db.fetch_assoc(out)
def
insertTableData(conn,rollno,username,email,pass word):
sql="INSERT INTO userdetails(rollno,username,email,password)
VALUES ({},'{}','{}','{}')".format(rollno,username,ema il,password)
out = ibm_db.exec_immediate(conn,sql)
print('Number of affected rows : ',ibm_db.num_rows(out),"\n")
def updateTableData(conn,rollno,username,email,pass word):
sql = "UPDATE userdetails SET (username,email,password)=('{}','{}','{}') WHERE
rollno={}".format(username,email,password,rolln o)
out = ibm_db.exec_immediate(conn, sql)
print('Number of affected rows : ', ibm_db.num_rows(out), "\n")
def deleteTableData(conn,rollno):
sql = "DELETE FROM userdetails WHERE rollno={}".format(rollno)
out = ibm_db.exec_immediate(conn, sql) print('Number of affected rows : ',
ibm_db.num_rows(out), "\n")
try:
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-
a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;Security=
SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ctb99199;PWD=GybYxLw1rH
z86oSh;","","")
print("Db connected")
except:
print("Error")
from flask import Flask,render_template,request,url_for,session
app=Flask(__name__)
@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
if request.method=="POST":
printTableData(conn) username=request.form['username']
password=request.form['password']
try: if dictionary[username] == password and username in dictionary: