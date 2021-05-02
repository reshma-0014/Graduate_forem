# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app=Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="reshma"
app.config['MYSQL_PASSWORD']="reshma2002"
app.config['MYSQL_DB']="user_details"
app.config['SECRET_KEY']="8a864e8bf7b1946f88279e61"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql=MySQL(app)
bcrypt = Bcrypt(app)

    
from forem import route   


