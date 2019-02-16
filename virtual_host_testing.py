import requests
import bs4
from bs4 import BeautifulSoup, SoupStrainer
import socket
import re
from List_of_index import list_of_virtual_host

def main(hostname):

	

	
	header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}
	try:
	
		ip = socket.gethostbyname(hostname)
		req = requests.post('https://www.ipaddress.com/reverse-ip-lookup', data={'host':ip}, headers=header)

		bs14 = BeautifulSoup(req.content, 'html.parser', parse_only=SoupStrainer('ol'))
		
		for link in bs14.findAll('a', attrs={'href': re.compile("^http://")}):
			new_link = link.get('href').replace('.ipaddress.com', '')
			
			list_of_virtual_host.append(new_link)
	except Exception as e:
		print e
	
	