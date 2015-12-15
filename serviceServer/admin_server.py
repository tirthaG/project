#***************service server*********************#

from bottle import route, run, request
from bottle import get, run
import bottle
from bottle import error
from bottle import static_file
import mysql.connector
import pymongo
import cgi
import re
import datetime
import random
import hmac
import user
import sys
import os

i=0


@bottle.post('/newNode')
def insert_entry():
    postdata = request.body.read()
    print postdata #this goes to log file only, not to client
    name,location=postdata.split("=",1)
    pwd="pwd"+name+location
    cnx=mysql.connector.connect(user="ideate",password='password',database='one')
    cursor=cnx.cursor()
    try:
        add_entry=("INSERT INTO data (name,location,pwd) VALUES (%s,%s,%s)")
	entry_data=(name,location,pwd)
	cursor.execute(add_entry,entry_data)
	cnx.commit()
	cursor.close()
	cnx.close()
	
	#add encryption

	return "1"
		
    except:
        print ("Error inserting post")
	return "0"



@bottle.post('/login') 
def do_login(): 
	postdata=request.body.read()
	uid,pwd=postdata.split("=",1)
	print uid+" "+pwd
	cnx=mysql.connector.connect(user="ideate",password='password',database='one')
    	cursor=cnx.cursor()
	cursor.execute("select uid,pwd from data where uid="+uid+" and pwd='"+pwd+"'")
	result=cursor.fetchone()
	if result : 
		return "1" 
	else: 
		return "0"


run(host='localhost', port=8080, debug=True)
