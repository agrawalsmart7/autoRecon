import socket	
import threading
from List_of_index import *
import ports_to_scans
from collections import OrderedDict



def dicta(newip, port):
		

	if newip in urls_returning200:
		dict200.setdefault(newip, [])
		dict200[newip].append(port)

		
	elif newip in urls_returning400:
		dict400.setdefault(newip, [])
		dict400[newip].append(port)
		
	elif newip in urls_returning401:
		dict401.setdefault(newip, [])
		dict401[newip].append(port)
		
		
	elif newip in urls_returning403:
		dict403.setdefault(newip, [])
		dict403[newip].append(port)
		
		
	elif newip in dictcname:
		dict404.setdefault(newip, [])
		dict404[newip].append(port)
					
def sockscan(ip, schemess, port, slash):
	
	try: 
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(3)
		
		result = sock.connect_ex((ip, port))
		newip = schemess+ip+slash
		
		if port == 21:
			if result == 0:
				
				print "\t [+]" + str(port)

				ftpurls.append(newip)
				
				
				dicta(newip, port)
			
							
		else:
			if result == 0:
				
				print "\t [+]" + str(port)
				dicta(newip, port)
			
			
		sock.close()
	except Exception as e:
		print e

def socketscan(y):
	
	schemess = 'http://'
	ports_to_scans.formate(y, schemess, sockscan)	
	
def printingofportscans():
	print  "\n...............................................................................................\n"	

	print "\n\n                                                 [PHASE: 4]: Starts below                                                \n\n"
	
	
def callforscanning(x):
	
	socketscan(x)

def executing_portscan():		
	
	print "[!]Finding the Port status of 200 status \n"
	for x in urls_returning200:
		callforscanning(x)
	
	
	print "\n[!]Finding the Port status of 400 status \n"		
	for x in urls_returning400:
			
		callforscanning(x)
		
	print "\n[!]Finding the Port status of 401 status \n"	
	for x in urls_returning401:
		
		callforscanning(x)
	print "\n[!]Finding the Port status of 403 status \n"
	for x in urls_returning403:
		
		
		callforscanning(x)
	
	print "\n[!]Finding the Port status of 404 status \n"
	for x in urls_returning404:
		
		callforscanning(x)
		