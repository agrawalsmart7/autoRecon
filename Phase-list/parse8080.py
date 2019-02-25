import requests
import bs4
from bs4 import BeautifulSoup
from List_of_index import json_dict
import threading
import json_output

infodict = {}

def run(domain, port):
	req = requests.get(domain+':'+str(port))
	infodict.setdefault(domain, [])
	if 'server' in req.headers:
	
		
		infodict[domain].append('Server: '+ req.headers.get('Server'))
		
	soup = BeautifulSoup(req.content, 'lxml')
	
	if soup.find('title'):
		
		infodict[domain].append('Title: '+ soup.find('title').text)
		
def parse8080():

	local_threads = []
	for key, value in json_dict.items():
		if '8080' in str(value[0]['openports']):
			th = threading.Thread(target=run, args=(key, '8080'))
			th.daemon = True
			local_threads.append(th)
			
	for threads in local_threads:
		threads.start()
		
	for threads in local_threads:
		threads.join()
	
	try:
	
		for domains, info in infodict.items():
			print "\n Host: ", domains
			print info[0]
			print info[1]
	except Exception as e:
		pass
	json_output.json_output('8080_info', infodict)	
		

	
	
