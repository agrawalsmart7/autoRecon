import dns.resolver
from dns.resolver import NXDOMAIN
from collections import OrderedDict
from List_of_index import *
import json_output

def printingofcnames():
	print "\n...............................................................................................\n"	
	print "\n\n                                                 [PHASE: 3]: Starts below                                                \n\n"	
		
	print "\n\n[!]Finding the CNAME's of 404 URL's\n"
	
def cnames(new_url, schemes):			
	


	try:
		
		answers = dns.resolver.query(new_url, 'CNAME')	
		
		
		print '\t ' +'\n[+]query qname:', answers.qname
		for rdata in answers:
			
			print '\t Cname Target Address:', rdata.target
			key = schemes + new_url
			
			
			rdata = str(rdata)
			rdata = rdata.translate(None, '[]<>')
			dictcname[key]=rdata
			
	
			
			
		
	except dns.resolver.NXDOMAIN:
		print "\t " +"\n[-]"+ str(new_url) + '-' + " Invalid domain"
		 
	except dns.resolver.Timeout:
		print "\t " +"\n[-]"+ str(new_url) + '-' + " Timed out while resolving"
	except dns.exception.DNSException:
		print "\t " +"\n[-]"+ str(new_url) + '-' + " Unhandled exception"
			
	
	
def executingcnames(urls_returning404):
	
	for y in urls_returning404:
		y = y.replace('www', '')
		if 'https://' in y:
			schemes = 'https://'
			new_url = y.replace("https://", "")
			cnames(new_url, schemes)
		else:
			schemes = 'http://'
			new_url = y.replace("http://", "")
			cnames(new_url, schemes)
			
	json_output.json_output('cname', dictcname)