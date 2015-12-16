#********service client************#

#this is the administrative daemon communicating with the service server
#1. initializes comm with the server(login or registration)
#2. maintain policy, app list as variables
#3. run listed apps
#4. in func run: update policy, run new apps
#5. repeat 4 acc. to policy

#testing for git

from os import fork
from time import sleep
import httplib, urllib
from os import path
from client import first_sync(), sync()
from subprocess import Popen
from client import first_sync, sync
from Crypto.PublicKey import RSA
from Crypto import Random

class Admin():
	def __init__(self):
		t=0	# time to get new policy
		uid=""	#extract from auth.txt, get from server
		pwd=""	#extract from auth.txt, get from server
		apps=[]	#list of apps, appid:serverip
		ip=""	#extract from server.txt
		app_handle=[]	#just in case
		i=0;		#counter
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
		info.close()
	
	def setParams(params):

	def getPolicy():
		#1
		#http request response get jason obj or something else
		#write code
		policy=open("policy.txt", "r+")
		policy.seek(0, 2)
		line="t:"+t
		policy.write(line)
		policy.close()

	def getApps():
		temp=apps
		#2
		#http request response get jason obj or something else
		#key:value  appId:serverIP
		return new	

	def initialize():
		
		#login
		if path.isfile("auth.txt"): 
			auth=open("auth.txt", "r")
			line=auth.readline()
			auth.close()	
			uid, pwd=line.split(":", 1)
			
			# add encryption to send pwd to server
			file=open("../../serviceServer/keys_server.txt","r")
			public_str=file.read()
			file.close()
			public_key=RSA.importKey(public_str)
			enc_data=public_key.encrypt(pwd, 32)

			params = urllib.urlencode({uid:enc_data})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(ip, 8080)
			conn.request("POST","/login",params ,headers)
			response=conn.getresponse()
			
			print response.status, response.reason
			st=response.read()
			print s1 

			if(s1=="1"):
				return 1
			else :
				return 0
		else:
		#registration

			random_num=Random.new().read
			keys=RSA.generate(1024,random_num)
			public_key=keys.publickey()
	

			file=open("keys_client.txt","w+")
			file.write(public_key.exportKey())
			file.close()
			
			params = urllib.urlencode({uname: loc})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(ip, 8080)
			conn.request("POST", "/newNode", params, headers)
			response = conn.getresponse()
			print response.status, response.reason
			pwd_enc=response.read()
			zero="0"
			if pwd_enc=zero:
				return 0
			#8
			#get uid(remaining), pwd
			line="uid:pwd"
			auth=open("auth.txt", "w")
			auth.write(line)
			auth.close()
			
			#9
			#check when to return 1
			return 1
	def startApp():
		# download appid.service file in correct location
		# download other files in the predefined location
		# how?
		# 5
		for app in apps
			service="App"+app[0]+".service"
			trash=Popen("systemctl", "enable", service)
			app_handle[i]=Popen("systemctl", "start", service)
			i=i+1
		
	def startApp(app):
		service=app[0]+".service"
		trash=Popen("systemctl", "enable", service)
		app_handle[i]=Popen("systemctl", "start", service)
		i=i+1

	def run():

		getPolicy()
		apps=getApps()
		startApp()
		pid=fork()
		if pid==0
			while True:
				getPolicy()
				new=getApps()
				#6
				#code considers addition of new apps
				#do we need to consider removal of already running apps
				for app in new:
					flag=0
					for app_old in apps:
						if app[0]==app_old[0]:
							flag=1
							break
					if !flag:
						apps.append(app)
						startApp(app)
				sleep(t)
					
admin=Admin()
ok=admin.initialize()
if ok:
	admin.run()
else:
	#7
	#print appropriate error from the server.
	print "error in login, registration"
