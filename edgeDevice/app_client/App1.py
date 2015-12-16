#***************application (content distribution) client*************************

from os import fork
from time import sleep
import httplib, urllib
from os import path
from subprocess import Popen

class App1():		
	t=3	#time to get new policy
	dt=0	#set in getPolicy()
	bw=0 	#set in getPolicy()
	uid=""	#extract from auth.txt, get from server
	pwd=""	#extract from auth.txt, get from server
	ip=""	#extract from server.txt
	wd=""
	uname=""
	loc=""

	def __init__(self):	
		#get server information
		server=open("server.txt", "r")
		line=server.readline()
		server.close()	
		trash, ip=line.split(":", 1)

		#get working directory
		wd=check_output("pwd")
		
		#get parameters of client 
		params=["", ""]
		info=open("info.txt", "r")	
		for line in info:
			key, val=line.split(":", 1)
			if key=="uname":
				params[0]=value
			else if key=="loc":
				params[1]=value
		info.close()
		uname=params[0]
		loc=params[1]


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

	def initialize(self):
		
		#3
		#check where to use in following code.
		
		#login
		if path.isfile("auth.txt"): 
			auth=open("auth.txt", "r")
			line=auth.readline()
			auth.close()	
			uid, pwd=line.split(":", 1)
			#4
			#check where to use in following code.

			params = urllib.urlencode({uid:pwd})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(self.ip, 8080)
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
			params = urllib.urlencode({uid: loc})
			headers = {"Content-type": "appication/x-www-form-urlencoded", "Accept": "text/plain"}
			conn = httplib.HTTPConnection(self.ip, 8080)
			conn.request("POST", "/newNode", params, headers)
			response = conn.getresponse()
			print response.status, response.reason
			print response.read()
			#8
			#get uid, pwd
			line=uid+":"+pwd
			auth=open("auth.txt", "w")
			auth.write(line)
			auth.close()
			
			#9
			#check when to return 1
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
