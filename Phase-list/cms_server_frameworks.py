from List_of_index import wadresults2, wadresults
import re
from bs4 import BeautifulSoup, SoupStrainer
import requests

ips = []

def histroy(domain):

	req = requests.get('https://securitytrails.com/domain/%s/history/a')%domain
	
	for x in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', req.content):
		ips.append(x)
		
	print "\n[+]DNS history FOUND for Domain:- %s:- \n" %domain
	for x in set(ips):
		
		print x

def printing_of_httpurlstates():
	print "\n.........................................................................."
	
	print "\n\n                                                 [PHASE: 5]: Starts below                                                \n\n"
	print "Finding the CMS's, Frameworks, Server of subdomains which have HTTP port open\n"
	return


def gettingkeyvalue(key, value):
	
	print "\t Host:- "+ key
	value= str(value).replace('/', ' ')
	value1 = value.strip('[]')
	print "\t Info:- "+ value1.strip("''"), "\n"		
		
def parsing_wadresults():

	for key, values in wadresults.iteritems():
		
		
		wadresults2.setdefault(key, [])
		
		for x in values:
			
			if x == '':
				None
			else:
				
				v1 = str(x).replace('/', ' ')	
				v2 = v1.strip('[]')
				wadresults2[key].append(v2)
				
def getting_results_from_httpurlstates():
	for key, value in wadresults2.iteritems():
		gettingkeyvalue(key, value)
				
			
			
def main():
	printing_of_httpurlstates()
	parsing_wadresults()
	getting_results_from_httpurlstates()
	
			