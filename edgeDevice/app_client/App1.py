#***************application (content distribution) client*************************

from os import fork
from time import sleep
import httplib, urllib
from os import path
from client import first_sync(), sync()
from subprocess import Popen
from client import first_sync, sync
from Crypto.PublicKey import RSA
from Crypto import Random

class App1():
	def __init__(self):
		t=3	#time to get new policy
		dt=0	#set in getPolicy()
		bw=0 	#set in getPolicy()
		uid=""	#extract from auth.txt, get from server
		pwd=""	#extract from auth.txt, get from server
		ip=""	#extract from server.txt
		wd=""
		uname=""
		loc=""
	
		#get server information
		server=open("server.txt", "r")
		line=server.readline()
		server.close()	
		trash, ip=line.split(":", 1)

		#get working directory
		wd=check_output("pwd")
		
		#get parameters of client 
		params=getParams()
		uname=params[0]
		loc=params[1]
		
	def getParams():
		params=["", ""]
		info=open("info.txt", "r")	
		for line in info:
			key, val=line.split(":", 1)
			if key=="uname":
				params[0]=value
			else if key=="loc":
				params[1]=value
		policy.close()
	
	def setParams(params):

	def getPolicy():		
		#1
		#http request response get jason obj or something else
		#write code
		policy=open("policy.txt", "r+")
		policy.seek(0, 2)
		line="bw:"+bw
		policy.write(line)
		line="dt:"+dt
		policy.write(line)
		policy.close()

	def initialize():
		
		#3
		#check where to use in following code.
		
		#login
		if path.isfile("auth.txt"): 
			auth=open("auth.txt", "r")
			line=auth.read()
			auth.close()	
			uid=line['uid']
			pwd=line['pwd']
			
			# encryption to send pwd to server
			file=open("../../appServer/keys_server.txt","r")
			public_str=file.read()
			file.close()
			public_key=RSA.importKey(public_str)
			enc_data=public_key.encrypt(pwd, 32)			

			params = urllib.urlencode({uid:enc_data})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection("localhost", 8080)
			conn.request("POST","/login",params ,headers)
			response=conn.getresponse()
			
			print response.status, response.reason
			st=response.read()
			print s1 
			s2="1"
			if(s1==s2):
				return 1
			else :
				return 0
		else:
		#registration	
			#encryption: generate keys
			random_num=Random.new().read
			keys=RSA.generate(1024,random_num)
			public_key=keys.publickey()

			file=open("keys_client.txt","w+")
			file.write(public_key.exportKey())
			file.close()
	
			params = urllib.urlencode({'avanti': 'pune'})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection("localhost", 8080)
			conn.request("POST", "/newNode", params, headers)
			response = conn.getresponse()
			print response.status, response.reason
			enc_data=response.read()
			dec_data=keys.decrypt(enc_data)
			zero="0"
			if dec_data=zero:
				return 0
			print dec_data
			json_obj=json.loads(dec_data)
			auth=open("auth.txt", "w")
			auth.write(json_obj)
			auth.close()
			return 1

	def run():
		#sync content			

		rsync="rsync"+"-rtv"+uname+"@"+ip+"::"+uname+"/data/"+wd+"/data/"
		str=pwd+"\n"
		run(rsync, events={'(?i)password': str})				
		getPolicy()

		hr=timedelta(hours=dt)
		days_1=timedelta(days=1)
		temp=datetime.now()
		temp+=days_1
		t=datetime(temp.year, temp.month, temp.day, 3, 0, 0)

		pid=fork()
		if pid==0:
			while(1):
				while(datetime.now()-t<hr):
					if(get_bw<bw):

						#sync content			
						rsync="rsync"+"-rtv"+uname+"@"+ip+"::"+uname+"/data/"+wd+"/data/"
						str=pwd+"\n"
						run(rsync, events={'(?i)password': str})				
		
						#get parameters from new policy
						getPolicy()
						hr.hours=dt	

						break
					sleep(15)
				temp=datetime.now()-t
				t=t+days_1-temp
				time.sleep((days_1-temp).total_seconds())	
				

client=App1()
ok=client.initialize()
if ok:
	client.run()
else:
	#7
	#print appropriate error from the server.
	print "error in login, registration"
