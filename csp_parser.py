import requests
import re
import bs4
from bs4 import BeautifulSoup, SoupStrainer
import colorama
import threading
import crayons
import time
from List_of_index import *

#from List_of_index import *

colorama.init()


def headers():
	UA = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}	
		
	return UA	

def jsonp_finder_ask(domain):
	ua = headers()
	
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
	ua = headers()
	dork = 'site:'+domain+' inurl:JSONP'
	url = 'https://www.google.co.in/search?filter=0&num=100&q=%s&start='%dork
	
	req2 = requests.get(url)
	
	bs = BeautifulSoup(req2.content, 'lxml')
	
	
	
	print "\n", (crayons.yellow('[!]')),("JSONp endpoints found from google (if any)")	
	for x in bs.findAll('cite'):
		print "\t", x.text
		jsonpurls.append(x.text)
		

for_jsonp_finder = []
		
def parsing_csp(xx, value):
	string = [xx + " 'self'",   xx + ' self'] 
	string2 = re.findall(r'\*+\.+\w+\.+\w+', value)
	string3 = re.findall(r'\w+\.+\w+\.+\w+', value)
	
	for y in string:
		if y in value:
			
			print "\t", (crayons.green(xx)) , " : " , (crayons.green('Self'))
			
	
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
	csp_directives = ['default-src', 'script-src' ,'img-src', 'frame-ancestors', 'frame-src']
	
	if 'Content-Security-Policy' in req.headers:
	
	
		header_value = req.headers.get('Content-Security-Policy')
		
		

		value = header_value.partition(';')
		print '\n\t CSP-Directive :  Value \n'
		
		if value[0]:
			
			for x in csp_directives:
				if x in value[0]:
					parsing_csp(x, value[0])
					
			if  value[2]:
				
				value2 = value[2].partition(';')
				
				for x in csp_directives:
					if x in value2[0]:
						
						parsing_csp(x, value2[0])
						
				
				if value2[2]:
					value3 = value2[2].partition(';')
					for x in csp_directives:
						if x in value3[0]:
							parsing_csp(x, value3[0])
					
					if value3[2]:
						value4 = value3[2].partition(';')
						
						for x in csp_directives:
							if x in value4[0]:
								
								parsing_csp(x, value4[0])
			
				
		
		search_pattern = re.findall( r'\*+\.+\w+\.+\w+', header_value)
		
		print "\n Target's CSP includes domains Self. So trying to find the JSONp endpoint on those domains. "
		
		for x in search_pattern:
			
			domain = x.replace('*.', '')
			for_jsonp_finder.append(x)
			
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
		
