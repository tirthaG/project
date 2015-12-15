#**********application (content distribution) server***********#

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

	#1. get uid
	#add entries into secrets file and conf file
	add_new(uid, pwd)
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

def add_new(uid, pwd):
	
	#update secrets file
	app="App"+str(uid)
	secrets=open("/etc/rsyncd.secrets", "r+")
	secrets.seek(0, 2)
	line=app+":"+pwd
	secrets.write(line)
	secrets.close()
	
	#create module for app in conf file
	wd=check_output("pwd")
	call(["mkdir", app+"/data"])
	
	conf=open("/etc/rsyncd.conf", "r+")
	conf.seek(0, 2)
	module="["+app+"]"
	conf.write(module)
	path="path="+wd
	conf.write(path)
	comment="comment=this folder belongs to edge device"+str(uid)
	conf.write(comment)
	uid="gid=nobody"
	conf.write(uid)
	gid="gid=nobody"
	conf.write(gid)
	read_only="read only=no"
	conf.write(read_only)
	li="list=yes"
	conf.write(li)
	auth_users="auth users="+app
	conf.write(auth_users)
	secret="secrets file="+wd+"/rsyncd.secrets"
	conf.write(secret)
	conf.close()
	

run(host='localhost', port=8080, debug=True)
