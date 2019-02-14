from List_of_index import *
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
				
				
def alloting_value_to_dict():
	wadresults_index_wise = list(wadresults.items())
		
	dict200_index_wise = list(dict200.items())
	dict400_index_wise = list(dict400.items())
	dict401_index_wise = list(dict401.items())
	dict403_index_wise = list(dict403.items())
	dict404_index_wise = list(dict404.items())
	

	for i in range(len(dict200)):
		try:
				
			for key, value in wadresults2.iteritems():
				
				if (key==dict200_index_wise[i][0]):
						
					getvalue200.setdefault(key, [])
					urlport= str(dict200_index_wise[i][1])
					
					getvalue200[key].append(urlport)
					value1 = str(value).strip('\r')
					getvalue200[key].append(value1)
					
		except IndexError as e:
			print e	
				
	for i in range(len(dict400)):
		
		
		try:
				
			for key, value in wadresults2.iteritems():
				if (key == dict400_index_wise[i][0] ):
						
					getvalue400.setdefault(dict400_index_wise[i][0], [])
					urlport= str(dict400_index_wise[i][1])
					
					getvalue400[dict400_index_wise[i][0]].append(urlport)
					value1 = str(value).strip('\r')
					getvalue400[dict400_index_wise[i][0]].append(value1)
					
		except IndexError as e:
			print e	
				
	for i in range(len(dict401)):
		
		
		try:
				
			for key, value in wadresults2.iteritems():			

				if (key == dict401_index_wise[i][0]):
						
					getvalue401.setdefault(dict401_index_wise[i][0], [])
					urlport= str(dict401_index_wise[i][1])
					
					getvalue401[dict401_index_wise[i][0]].append(urlport)
					value1 = str(value).strip('\r')
					getvalue401[dict401_index_wise[i][0]].append(value1)
					
		except IndexError as e:
			print e	
				
	for i in range(len(dict403)):
		
		
		try:
				
			for key, value in wadresults2.iteritems():					
				if (key == dict403_index_wise[i][0]):
						
					getvalue403.setdefault(dict403_index_wise[i][0], [])
					urlport= str(dict403_index_wise[i][1])
					
					getvalue403[dict403_index_wise[i][0]].append(urlport)
					value1 = str(value).strip('\r')
					getvalue403[dict403_index_wise[i][0]].append(value1)
					
		except IndexError as e:
			print e	
					
	for i in range(len(dict404)):
		
		
		try:
				
			for key, value in wadresults2.iteritems():				
				
				if (key == dict404_index_wise[i][0] ):
						
					getvalue404.setdefault(dict404_index_wise[i][0], [])
					urlport= str(dict404_index_wise[i][1])
					
					getvalue404[dict404_index_wise[i][0]].append(urlport)
					value1 = str(value).strip('\r')
					getvalue404[dict404_index_wise[i][0]].append(value1)
					
		except IndexError as e:
			print e	
			
			
def main():
	printing_of_httpurlstates()
	parsing_wadresults()
	getting_results_from_httpurlstates()
	alloting_value_to_dict()
			