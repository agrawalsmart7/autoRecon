import requests
from List_of_index import *
import threading
import time


thread_for_files = []

def searching_for_url(x, filename, urls_interesting_files):
	try:
	
		newurl = x+'/'+filename

		request = requests.get(newurl)
		if (request.status_code == 200):
			
			urls_interesting_files.append(newurl)
	except Exception as e:
		print e, ' on this domain ', x

def exect(url, urls_interesting_files):
	local_threads = []
	with open('check_default_files.txt') as file:
		
		for filename in file:
			
			th1 = threading.Thread(target=searching_for_url, args=(url, filename, urls_interesting_files))
			th1.daemon = True
			local_threads.append(th1)
			
			
			'''searching_for_url(url, filename, urls_interesting_files)'''
	for x in local_threads:
		thread_for_files.append(x)
		
	

	
def main(urls_interesting_files):

	for x in urls_returning200:
		exect(x, urls_interesting_files)
		
	for x in urls_returning403:
		exect(x, urls_interesting_files)	
	
	for x in urls_returning404:
		exect(x, urls_interesting_files)
		
	for x in thread_for_files:
		x.start()
		time.sleep(0.2)
		
	for x in thread_for_files:
		x.join()
