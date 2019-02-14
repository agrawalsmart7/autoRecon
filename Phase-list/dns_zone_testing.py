import dns.resolver
import dns.query
import dns.zone
from List_of_index import *


ns = []

def exce(domain):
	try:
	
		answers = dns.resolver.query(domain,'NS')
		for server in answers:
			
			ns.append(server.target)
	except dns.resolver.NoNameservers:
		if debug:
			print domain+' has no servers'
	except dns.resolver.NoAnswer:
		if debug:
			print host+' no Answer'
			
	except Exception, e:
		print e

def main(hostname):
	try:
	
		exce(hostname)
		for x in ns:
			
			
			z = dns.zone.from_xfr(dns.query.xfr(str(x), hostname))
			
			names = z.nodes.keys()
			names.sort()
			for n in names:
				if 'SOA' in z[n].to_text(n):
					dns_zone_vul_domains.append(x) #output this into output file.
					
			
	except Exception as e:
		pass