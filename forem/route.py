from forem import app
from flask import render_template,request,redirect,url_for,flash
from forem.forms import RegisterForm,LoginForm
from forem import mysql,bcrypt
from flask_mysqldb import MySQLdb
@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html')


@app.route('/forem')
def forem_page():
    return render_template('forem.html')


password_hash=" "
@app.route('/register',methods=['GET','POST'])
def register_page():
   form = RegisterForm()
   if form.validate_on_submit():
           username=request.form['username']
           email=request.form['email_address']
           password=request.form['password1']
           uid=4
           password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

           
           cur=mysql.connection.cursor()
           
           cur.execute("INSERT INTO user (id,username,email_address,password_hash) VALUES (%s,%s,%s,%s)",(uid,username,email,password_hash))
           
           mysql.connection.commit()
           
           cur.close()
           
           return redirect(url_for('forem_page'))
   if form.errors !={}:
       for err_msg in form.errors.values():
           flash(f'There was an error in creating account:{err_msg}', category='danger')
   return render_template('register.html',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user=request.form['username']
        attempted_password=request.form['password']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cur.execute("SELECT username,password_hash FROM user")
        result=cur.fetchall()
        
        count=1 
        i=0
        for (username_check,password_check) in cur:
             values=result[i].values()
             result_list=list(values)
             print(result_list[1])
             i=i+1
             if result_list[0]==attempted_user and bcrypt.check_password_hash(result_list[1],attempted_password):
                   count=0
                   flash(f'Success!! you have logged in successfully as {attempted_user}', category='success')
            
                   return redirect(url_for('forem_page'))
        if count==1:
            flash('Username and password does not match, please try again', category='danger')
        cur.close()
            
    return render_template('login.html', form=form)

if __name__ =="__main__":
    app.run(debug=False)
