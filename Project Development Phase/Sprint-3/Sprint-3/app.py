import ibm_db
import re
from flask import Flask, render_template, request, redirect, url_for, session,flash

app = Flask(__name__)
app.secret_key="i don't care"
myconn=ibm_db.connect('DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=ytl86182;PWD=IwLcHrD3CEMU2chS', '', ''
	)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        
        query = 'SELECT * FROM admin WHERE username =?;'
        stmt=ibm_db.prepare(myconn,query)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[a-z0-9]+', username):
            msg = 'name must contain only lowercase characters and numbers !'
        else:
            query = "INSERT INTO ADMIN (username,password) VALUES (?,?)"
            stmt=ibm_db.prepare(myconn,query)
            ibm_db.bind_param(stmt,1,username)
            ibm_db.bind_param(stmt,2,password)
            ibm_db.execute(stmt)
            msg = 'You have successfully registered !'
            return render_template('login.html', msg = msg)
	



@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
	if request.method=="POST":
		Username=request.form['Username']
		Password=request.form['Password']
		query="select * from admin where username=? and password=?;"
		stmt=ibm_db.prepare(myconn, query)
		ibm_db.bind_param(stmt, 1, Username)
		ibm_db.bind_param(stmt, 2, Password)
		ibm_db.execute(stmt)
		data=ibm_db.fetch_assoc(stmt)
		if data:
			session['loggedin']=True
			return  render_template('cognos.html')
		
		else:
			flash("Incorrect Username or Password")
	return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)