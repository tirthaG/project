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
from Crypto.PublicKey import RSA
from Crypto import Random

i=0


@bottle.post('/newNode')
def insert_entry():
	postdata = request.body.read()
   	print postdata #this goes to log file only, not to client
    	name,location=postdata.split("=",1)
    	pwd="pwd"+name+location

	#encryption
    	file=open("../edgeDevice/admin/keys_client.txt","r")
	public_str=file.read()
	file.close()
	

	#entering into db
    	cnx=mysql.connector.connect(user="ideate",password='password',database='one')
    	cursor=cnx.cursor()
    	try:
        	add_entry=("INSERT INTO data (name,location,pwd) VALUES (%s,%s,%s)")
		entry_data=(name,location,pwd)
		cursor.execute(add_entry,entry_data)
		cursor.execute("select uid from data where pwd='"+pwd+"'")
		uid=cursor.fetchone()
		print uid[0]
		cnx.commit()
		cursor.close()
		cnx.close()
		# concat uid to enc_pwd
		string={"uid":uid[0],"pwd":pwd}
		print string
		jdata=json.dumps(string)
		public_key=RSA.importKey(public_str)
		enc_data=public_key.encrypt(jdata, 32)
    		return enc_data
		
		
    	except:
        	print ("Error inserting post")
		return "Invalid"



@bottle.post('/login') 
def do_login(): 
	random_num1=Random.new().read
	keys1=RSA.generate(1024,random_num1)
	public_key1=keys1.publickey()
	
	#creating server keys
	file=open("keys_server.txt","w+")
	file.write(public_key1.exportKey())
	file.close()
	#reading encrypted data from client 
	postdata=request.body.read()
	uid,enc_pwd=postdata.split("=",1)
	#decrypting pwd
	pwd=keys1.decrypt(enc_pwd)
	
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
