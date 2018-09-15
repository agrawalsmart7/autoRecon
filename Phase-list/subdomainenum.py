import subprocess
import optparse
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import bs4
from bs4 import BeautifulSoup, SoupStrainer
from collections import OrderedDict
import requests
import cname_finder
from List_of_index import *



headers = ['X-powered', 'X-generator', 'server','X-powered-by']




def find_from_sublister(hostname, filename):
	

	print "\n\n                                                 [PHASE: 1]: Starts below                                                 \n\n"
	print "\n[!][!]Getting Subdomains from Sublister\n\n\n\n"
	try:
		
	
		subdomain = subprocess.check_output(['python', 'sublist3r/sublist3r.py', '-d',hostname, '-o', filename]) 
		
		fopen = open(filename, 'r')
		print '[+]Saving results to:- ', filename
		print '[+]List of subdomain found \n'
		for x in subdomain.split('\n'):
			
			if '|' in x:
				None
			elif '__' in x:
				None
					
			elif '#' in x:
				None
			else:
				if 	'[-]' in x:
					None
				elif '[!]' in x:
					None
				elif '[~]' in x:
					None
				elif ' ' in x:
					None
				else:
					
					
					print x
					
		print "\n......................................................................................" 
		print "\n\n                                                 [PHASE: 2]: Starts below                                                 \n\n"
		print "[!!] Unavailable Subdomains\n"
		
		return fopen.readlines()
				
		
	
		
		
	except Exception as e:
		print "\nSomething went wrong"	
		print e
		
def httpurlstates(y, req):	
	try:
		
		wadresults.setdefault(y, [])
	
		parse = BeautifulSoup(req.content, 'html.parser', parse_only=SoupStrainer('meta'))
		
		for link in parse:
			if link.has_attr('name'):
				if 'generator' in link['name']:
					wadresults[y].append(link['content'])
				else:
					None
					
		for x in headers:
			if x in req.headers:
				value = req.headers.get(x)
				
				wadresults[y].append(value)
				
			else:
				wadresults[y].append('')
				

		

	except Exception as e:
		print "\t Can' find on this URL ", y ,e	

def urlrequests(ur):
	try:
		
		
		req = requests.get(ur)
		if req.status_code == responsecode[0]:
			urls_returning200.append(ur)
			
		elif req.status_code == responsecode[1]:
			urls_returning400.append(ur)
			
		elif req.status_code == responsecode[2]:
			urls_returning401.append(ur)	
			
		elif req.status_code == responsecode[3]:
			urls_returning403.append(ur)
			
		elif req.status_code == responsecode[4]:
			urls_returning404.append(ur)
		httpurlstates(ur, req)
	except requests.exceptions.RequestException as e:
		print ur
	



def executing_subdomains(newurllist, hostname, filename):
	
	for x in set(find_from_sublister(hostname, filename)):
		url = x.strip('\n\r')
		newurl = "http://" + url
		
		newurllist.append(newurl)
		
	with ThreadPoolExecutor(max_workers=20) as pool:
		list(pool.map(urlrequests,newurllist))
	
	

	
	print "\n\n[!]List of Urls's status Code is 200\n"
	for x in urls_returning200:
		
		print "\t"+ x
		
		
	print "\n\n[!]List of Urls's status Code is 400\n"	
	for x in urls_returning400:
	
		print "\t"+ x
		
		
	print "\n\n[!]List of Urls's status Code is 401\n"	
	for x in urls_returning401:
		
		print "\t"+ x
	

	print "\n\n[!]List of Urls's status Code is 403\n"	
	for x in urls_returning403:
		
	
		print "\t"+ x
		
	print "\n\n[!]List of Urls's status Code is 404\n"
	for x in urls_returning404:
		
		print "\t"+ x
			

	cname_finder.printingofcnames()
	cname_finder.executingcnames(urls_returning404)
	
	

	
	
