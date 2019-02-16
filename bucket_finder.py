import requests
import json_output
from bs4 import BeautifulSoup, SoupStrainer
import time
import threading
from List_of_index import *
import crayons

colorama.init()


ua = {"User-Agent ": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
github = []


def bing_search(domain):
	url = "https://www.bing.com/search?q=amazonaws.com+uber.com&qs=n&form=&sp=-1&pq=amazonaws.com+%s&sc=0-22&sk=&cvid=" %domain
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'lxml')
	for x in soup.findAll('cite'):
		
		string = str(x).replace('<strong>', '').replace('</strong>', '').replace('<cite>', '').replace('</cite>', '')
		if "s3.amazonaws.com" in string:
			buckets.append(string)			
			
			
def ask_search(domain):
	url = "https://www.ask.com/web?q=site:amazonaws.com+inurl:%s&o=0&qo=homepageSearchBox" %domain
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'lxml')
	for x in soup.findAll('p'):
		if x.has_attr('class'):
			if "PartialSearchResults-item-url" in x.get('class'):
				buckets.append(x.text)
				
				
def google_search(domain):

	#Debug this after some time
	
	url = "https://www.google.com/search?client=firefox-b-d&q=site:amazonaws.com+inurl:%s" %domain
	req = requests.get(url, headers=ua)
	soup = BeautifulSoup(req.content, 'lxml')
	
	for x in soup.findAll('cite'):
		
		if x.has_attr('class'):
			if "iUh30" in x.get('class'):
				buckets.append(x.text)
				
				
	
#def github_search(domain):
#	url = 'https://github.com/search?q="%s"+ API_Key'%domain
#	req = requests.get(url)
#	soup = BeautifulSoup(req.content, 'lxml')
#	for x in soup.findAll('a'):
#		if x.has_attr('rel'):
#			string= str(x).replace('<em>', '').replace('</em>', '')
#			if "nofollow" in x.get('rel'):
#				print x.text
					
				
def main(domain):
	t1 = threading.Thread(bing_search(domain))
	t2 = threading.Thread(ask_search(domain))
	t3 = threading.Thread(google_search(domain))
	
	t1.start()
	t2.start()
	t3.start()
	
	time.sleep(0.1)
	t1.join()
	t2.join()
	t3.join()
	
	print "\n" + crayons.green( "List of buckets found") + "\n "
	
	for x in buckets:
		print "\t "+ x
	



