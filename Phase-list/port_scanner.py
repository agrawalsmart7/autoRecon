import socket	
import threading
from List_of_index import *
import ports_to_scans
from collections import OrderedDict
import json_output
import json
dict_urls = {}


	

def dicta(newip, port):

	dict_urls.setdefault(newip, [])
	dict_urls[newip].append(port)
	
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
	
	print "\n[!] Starting Port Scanner.............\n"
	
	
	for key, value in json_dict.items():
		print "\n Host:- "+ key +"("+str(value[0]['statuscode'])+")"
		callforscanning(key)

	json_output.json_output('openports', dict_urls)
	
	