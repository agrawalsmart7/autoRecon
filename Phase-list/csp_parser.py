import requests
import re
import bs4
from bs4 import BeautifulSoup, SoupStrainer
import colorama
import threading
import crayons
import time
from List_of_index import *


colorama.init()


def jsonp_finder_ask(domain):
	
	
	dork = 'site:'+domain+' inurl:JSONP'
	url = 'https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=%s' %dork
	
	
	req = requests.get(url)
	
	bs = BeautifulSoup(req.content, 'lxml')
	
	
	print "\n", (crayons.yellow('[!]')),("JSONp endpoints URls from Ask.com (if any)")	
	
	for x in bs.findAll('p'):
		
		if x.has_attr('class'):
			
			if 'PartialSearchResults-item-url' in x.get('class'):
				print "\t", x.text
				jsonpurls.append(x.text)
	
def jsonP_finder_google(domain):

	dork = 'site:'+domain+' inurl:JSONP'
	url = 'https://www.google.co.in/search?filter=0&num=100&q=%s&start='%dork
	
	req2 = requests.get(url)
	
	bs = BeautifulSoup(req2.content, 'lxml')
	
	
	
	print "\n", (crayons.yellow('[!]')),("JSONp endpoints found from google (if any)")	
	for x in bs.findAll('cite'):
		print "\t", x.text
		jsonpurls.append(x.text)
		

for_jsonp_finder = []
		
def parsing_csp(xx, value, domain):
	string = [xx + " 'self'",   xx + ' self'] 
	
	string2 = re.findall(r'\w+\.+\w+', value)
	string3 = re.findall(r'\w+\.+\w+\.+\w+', value)
	
	for y in string:
		
		if y in value:
			
			print "\t", (crayons.green(xx)) , " : " , (crayons.green('Self'))
			for_jsonp_finder.append(domain)
	
	for x in string2:
		
		if x in value:
			
			
			print "\t",  (crayons.green(xx)), " : " , (crayons.green(x))
			
			for_jsonp_finder.append(x)
	for x in string3:
		
		if x in value:
			for_jsonp_finder.append(x)
			print "\t",  (crayons.green(xx)), " : " , (crayons.green(x))		
		



def check_cspheader(domain):
	
	url = 'http://'+domain
	
	req = requests.get(url)
	csp_directives = ['default-src', 'script-src','img-src', 'frame-ancestors', 'frame-src']
	
	if 'Content-Security-Policy' in req.headers:
	
	
		header_value = req.headers.get('Content-Security-Policy')
		
		

		value = header_value.partition(';')
		print '\n\t CSP-Directive :  Value \n'
		
		if value[0]:
			
			for x in csp_directives:
				if x in value[0]:
					parsing_csp(x, value[0], domain)
					
			if  value[2]:
				
				value2 = value[2].partition(';')
				
				for x in csp_directives:
					if x in value2[0]:
						
						parsing_csp(x, value2[0], domain)
						
				
				if value2[2]:
					value3 = value2[2].partition(';')
					for x in csp_directives:
						if x in value3[0]:
							parsing_csp(x, value3[0], domain)
					
					if value3[2]:
						value4 = value3[2].partition(';')
						
						for x in csp_directives:
							if x in value4[0]:
								
								parsing_csp(x, value4[0], domain)
			
				
		
		
		
		print "\n Target's CSP includes domains Self. So trying to find the JSONp endpoint on those domains. "
		
		
			
	else:
		print '\n', crayons.red('[-]'),'The target is not using CSP. Hence skipping this step\n'
		
		
def json_finder_executor():
	for domain in set(for_jsonp_finder):
	
		print "\n Domain:- " + domain
		
		t1 = threading.Thread(target=jsonP_finder_google, args=(domain,))
		t1.daemon= True
		
		t2 = threading.Thread(target=jsonp_finder_ask, args=(domain,))
		t2.daemon = True
		
		t1.start()
		time.sleep(0.1)
		t2.start()
		t2.join()

def main(domain):
	check_cspheader(domain)
	json_finder_executor()
