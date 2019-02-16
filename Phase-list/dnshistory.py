import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
from List_of_index import json_dict
import json_output

history_ips = {}


def histroy(domain):
	
	
	UA = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
	}
	newdomain = domain.replace('http://', '')
	req = requests.get('https://securitytrails.com/domain/%s/history/a' %newdomain, headers=UA)
	print "\n[+]DNS history for:- %s:- " %domain, 'if any '
	
	for x in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', req.content):
		history_ips.setdefault(domain, [])
		xx = "<a href='http://%s'>%s</a>"%(x, x)
		history_ips[domain].append(xx)
		
	
	
	
	
		
def main():
	print "\n Out-put will be save in the results. Note: You may seen blank because may be no domain using Cloudflare \n"
	for key, value in json_dict.items():
		for server in value[0]['server']:
			
			if server == 'cloudflare':
				
				histroy(key)
				
				
	json_output.json_output('Dns_history', history_ips)		

		