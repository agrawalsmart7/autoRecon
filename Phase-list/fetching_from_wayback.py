from List_of_index import *
import requests
import json
import threading
import os
import time
import json_output

localdict = {}

def printing_of_webarchieve():
	print "\n...............................................................................................\n"
	print "\n\n                                                 [PHASE: 7]: Starts below                                                \n\n"
	print "[!]Finding URL's in Wayback machine\n\n"
	
	
def archiveweb(domain, year):
		
	url = "https://web.archive.org/__wb/calendarcaptures?url={0}&selected_year={1}" .format(domain, year)

	try:
		
		req = requests.get(url)
		
		for x in json.loads(req.content):
			for y in x:
				for z in y:
					if 'ts' in str(z):
						for url_date in z['ts']:
							domain2 = domain.replace('http://', '')
							urls = "https://web.archive.org/web/{0}/{1}" .format(url_date, domain2)
							
							localdict.setdefault(domain, [])
							localdict[domain].append(urls)
							
							if domain in urls_returning401:
								
								webarchive_urls401.append(urls)
								
							elif domain in urls_returning403:
								
								webarchive_urls403.append(urls)
								
	except requests.exceptions.ConnectionError as e:
		pass
	
	except Exception as e:
		pass
		
def way_back_starting(yearlist, x):
	
	for y in yearlist:
		
		th1 = threading .Thread(target=archiveweb, args=(x, y))
		th1.daemon = True
		threadsforwayback.append(th1)		
		
def executing_wayback():
	
	for x in urls_returning401:
		way_back_starting(yearlist, x)
		
		
	for x in urls_returning403:
		print x
		way_back_starting(yearlist,x)
	
	
	for x in threadsforwayback:
		x.start()
		time.sleep(0.2)
		
	for x in threadsforwayback:
		x.join()	
		
	
def main():
	printing_of_webarchieve()
	executing_wayback()
	

	json_output.json_output('waybackurls', localdict)