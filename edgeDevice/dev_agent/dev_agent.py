#********service client************#

#this is the administrative daemon communicating with the service server
#1. initializes comm with the server(login or registration)
#2. maintain policy, app list as variables
#3. run listed apps
#4. in func run: update policy, run new apps
#5. repeat 4 acc. to policy

#testing for git
<<<<<<< HEAD
import base64
from os import fork
from time import sleep
import httplib, urllib,json
from os import path

from subprocess import Popen

from Crypto.PublicKey import RSA
from Crypto import Random

=======

from os import fork
from time import sleep
import httplib, urllib
from os import path
from client import first_sync(), sync()
from subprocess import Popen
from client import first_sync, sync
from Crypto.PublicKey import RSA
from Crypto import Random
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
from subprocess import Popen, check_output


class Admin():

	t=0	# time to get new policy
	uid=""	#extract from auth.txt, get from server
	pwd=""	#extract from auth.txt, get from server
	apps=[]	#list of apps, appid:serverip
	ip=""	#extract from server.txt
	app_handle=[]	#just in case
	i=0;		#counter
	uname=""
	loc=""

	def __init__(self):

		
		#get server information
		server=open("server.txt", "r")
		line=server.readline()
		server.close()	
		trash, ip=line.split(":", 1)
		print ip

		#get working directory
		wd=check_output("pwd")
		
		#get parameters of client 
		params=["", ""]
		info=open("info.txt", "r")	
		for line in info:
			key, val=line.split(":", 1)
			if key=="uname":
				params[0]=val
			elif key=="loc":
				params[1]=val
		info.close()
<<<<<<< HEAD
		self.uname=params[0]
		self.loc=params[1]
		
		

	def setParams(self,params):
		return

	def getPolicy(self):
		#1
		#http request response get jason obj or something else
		#write code
		#policy=open("policy.txt", "r+")
		#policy.seek(0, 2)
		#line="t:"+t
		#policy.write(line)
		#policy.close()
		t=5

	def getApps(self):
=======
		uname=params[0]
		loc=params[1]

	def setParams(params):
		return

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
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
		temp=apps
		#2
		#http request response get jason obj or something else
		#key:value  appId:serverIP
		return new	

	def initialize(self):
		
		#login
		if path.isfile("auth.txt"): 
<<<<<<< HEAD
			# read json object form auth-> kshitish
			#auth=open("auth.txt", "r")
			#line=auth.read()	
			#self.uid=line['uid']
			#self.pwd=line['pwd']
			self.uid=120
			self.pwd="pwdcocomum"
=======
			auth=open("auth.txt", "r")
			line=auth.read()
			auth.close()	
			uid=line['uid']
			pwd=line['pwd']
			
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
			# add encryption to send pwd to server
			file=open("../../serviceServer/keys_server.txt","r")
			public_str=file.read()
			file.close()
			public_key=RSA.importKey(public_str)
<<<<<<< HEAD
			enc_data=public_key.encrypt(self.pwd, 32)
			

			params = urllib.urlencode({self.uid:enc_data})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection("localhost", 8080)
=======
			enc_data=public_key.encrypt(pwd, 32)

			params = urllib.urlencode({uid:enc_data})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(self.ip, 8080)
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
			conn.request("POST","/login",params ,headers)
			response=conn.getresponse()
			
			print response.status, response.reason
			st=response.read()
<<<<<<< HEAD
			print st 

			if(st=="1"):
=======
			print s1 

			if(s1=="1"):
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
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
<<<<<<< HEAD
			print "check"
			name=self.uname.strip()
			print name
			location= self.loc.strip()
			
			params = urllib.urlencode({name: location})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection("localhost", 8080)
=======
			
			params = urllib.urlencode({self.uname: self.loc})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(self.ip, 8080)
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
			conn.request("POST", "/newNode", params, headers)
			response = conn.getresponse()
			print response.status, response.reason
			enc_data=response.read()
<<<<<<< HEAD
			print enc_data
			dec_data=keys.decrypt(enc_data)
			zero="0"
			if dec_data==zero:
				return 0
			print dec_data
			json_obj=json.loads(dec_data)
			with open("auth.txt", "w") as auth:
			#auth.write(json_obj)
				json.dump(json_obj,auth)
			auth.close()
			return 1
	def startApp(self):
=======
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
	def startApp():
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
		# download appid.service file in correct location
		# download other files in the predefined location
		# how?
		# 5
		for app in apps:
			service="App"+app[0]+".service"
			trash=Popen("systemctl", "enable", service)
			app_handle[i]=Popen("systemctl", "start", service)
			i=i+1
		
<<<<<<< HEAD
	def startApp(self,app):
=======
	def startApp(app):
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
		service=app[0]+".service"
		trash=Popen("systemctl", "enable", service)
		app_handle[i]=Popen("systemctl", "start", service)
		i=i+1

<<<<<<< HEAD
	def run(self):

		self.getPolicy()
		apps=self.getApps()
		self.startApp()
		pid=fork()
		if pid==0:
			while True:
				self.getPolicy()
				new=self.getApps()
=======
	def run():

		getPolicy()
		apps=getApps()
		startApp()
		pid=fork()
		if pid==0:
			while True:
				getPolicy()
				new=getApps()
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
				#6
				#code considers addition of new apps
				#do we need to consider removal of already running apps
				for app in new:
					flag=0
					for app_old in apps:
						if app[0]==app_old[0]:
							flag=1
							break
					if not flag:
						apps.append(app)
<<<<<<< HEAD
						self.startApp(app)
=======
						startApp(app)
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
				sleep(t)
					
admin=Admin()
ok=admin.initialize()

if ok:
<<<<<<< HEAD
	#admin.run()
	print "DONE"
=======
	admin.run()
>>>>>>> 0d5fd571524c50b9e26f111206497212b94b251e
else:
	#7
	#print appropriate error from the server.
	print "error in login, registration"
