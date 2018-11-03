import requests
from bs4 import BeautifulSoup, SoupStrainer
import sys
import re
import urlparse
from urlparse import urlunparse, parse_qs
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import crayons
import colorama

colorama.init()

urls = []
url_list = []
query_wale_urls = []
urls_for_xss = []
vulnerable = []
strips = []

def crawler(domain, bs):

	for link in bs.findAll('a'):
		x = link.get('href')
		urls.append(x)

	protocols = ['https://', 'http://']	

	for x in urls:
		for y in protocols:
			if y  in str(x):
				if domain in str(x):
					parse = urlparse.urlparse(x)
					
					if parse.query == "":
						url_list.append(x)
					else:
						query_wale_urls.append(x)
					
				
		if re.match(r'^/', str(x)):
			parse = urlparse.urlparse(x)
			
			
			if parse.query == "":
				url_list.append('http://'+domain+x)
			else:
				query_wale_urls.append('http://'+domain+x)
			




def url_parser(url):

	trigger = 'aa">xsstest<xsstest'
	parsed = urlparse.urlparse(url)
	querys = parsed.query.split("&")

	resuls = parse_qs(parsed.query)


	new_query = "&".join([ "{}{}".format(query, trigger) for query in querys])
	parsed = parsed._replace(query=new_query)

	url = urlunparse(parsed)
	urls_for_xss.append(url)


def xss_check(url):
	trigger = 'aa">xsstest<xsstest'
	req = requests.get(url)
	if trigger in req.content:
		
		vulnerable.append(url)
		
	elif 'aa">xsstest' in req.content:
		
		strips.append(url)
	
	else:
		None

		

def executor():


	with ThreadPoolExecutor(max_workers=5) as pool:
		list(pool.map(url_parser, query_wale_urls))
		


	with ThreadPoolExecutor(max_workers=5) as pool:
		list(pool.map(xss_check, urls_for_xss))

	for x in vulnerable:
		print '\n', crayons.green('[+]'), crayons.red('Vulnerable to XSS found:- '), x
		
		
	for x in strips:
		print '\n', crayons.green('[+]'), crayons.red('Partly Vulnerable, some using strip filters :- '), x		
		
		
		
def main(domain):
	
	url = 'http://'+domain
	req = requests.get(url)


	bs = BeautifulSoup(req.content, "html.parser", parse_only=SoupStrainer('a'))
	crawler(domain, bs)		
	executor()
	
	
	
