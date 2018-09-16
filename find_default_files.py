import requests
from List_of_index import *
import threading
import time


thread_for_files = []

def searching_for_url(x, filename, urls_interesting_files_open):
	newurl = x+'/'+filename

	request = requests.get(newurl)
	if (request.status_code == 200):
		urls_interesting_files_open.append(newurl)
		

def main(url, urls_interesting_files_open):
	with open('check_default_files.txt') as file:
		for filename in file:
			th1= threading.Thread(target=searching_for_url, args=(url, filename, urls_interesting_files_open))
			th1.daemon= True
			thread_for_files.append(th1)
			
		for threads in thread_for_files:
			threads.start()
			time.sleep(0.2)
			
		for threads in thread_for_files:
			threads.join()