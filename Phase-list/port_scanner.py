import socket	
from List_of_index import ftpurls, json_dict
import ports_to_scans
import json_output
import re
import time
dict_urls = {}
banner = {}



def dicta(newip, banner):

	
	dict_urls.setdefault(newip, [])
	dict_urls[newip].append(banner)
	
def sockscan(ip, schemess, port, slash):
	
	try: 
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(3)
		
		result = sock.connect_ex((ip, port))
		newip = schemess+ip+slash
	except Exception as e:
		print e, port	
		
		
		
	if port == 21:
		if result == 0:
			
			print "\t [+]" + str(port)
			ftpurls.append(newip)
			try:
			
				banner1 = str(sock.recv(4096))
				banner.setdefault(port, [])
				banner[port].append(banner1)
				
			except Exception as e:
				dicta(newip, port)
			
		
	
	elif port == 3306:
	
		
		if result == 0:
			
			print "\t [+]" + str(port)
			
			try:
				string = re.findall(r'\d+\.+\d+\.+\d+', str(sock.recv(4096)))
				if not string:
					pass
				else:
					for x in string:
				
						banner.setdefault(port, [])
						banner[port].append(x)
				
			except Exception as e:
				dicta(newip, port)
				
			
	else:
		if result == 0:
			print "\t [+]" + str(port)
			try:
			
				
				banner3 = str(sock.recv(4096))
				 
				banner.setdefault(port, [])
				banner[port].append(banner3)
				
				
					
				
			except Exception as e:
				dicta(newip, port)
				
		
	sock.close()
	

def socketscan(y):
	
	schemess = 'http://'
	ports_to_scans.formate(y, schemess, sockscan)	
	
def printingofportscans():
	print  "\n...............................................................................................\n"	

	print "\n\n                                                 [PHASE: 4]: Starts below                                                \n\n"
	
	
def callforscanning(x):
	
	socketscan(x)

def executing_portscan():		
	
	print "\n[!] Starting Port Scanner(with Service Banner).............\n"
	
	
	for key, value in json_dict.items():
		print "\n ----------------------", "\n"
		print "\t Host: ", key , '(',value[0]['statuscode'],') \n' 
		callforscanning(key)
		if not banner:
			pass
		else:
		
			dicta(key, banner)
		
	time.sleep(2)	
	
	json_output.json_output('openports', dict_urls)
	
