from List_of_index import dns_zone_vul_domains, list_of_virtual_host
import dns_zone_testing
import find_default_files
import virtual_host_testing
import csp_parser
import crayons
import colorama
import crawler
import bucket_finder

colorama.init()

def run(hostname):
	
	print "Target:- ", hostname, '\n'
	
	dns_zone_testing.main(hostname)
	if not dns_zone_vul_domains:
	
		print "  "+ " [+]Checking DNS Zone transfer leakage:- No" + "\n" 
		
	else:
		print "  "+ " [+]Checking DNS Zone transfer leakage:- Yes (leakage)"  + "\n"
	
	
	virtual_host_testing.main(hostname)

	if not list_of_virtual_host:
		print "  "+ " [+]Checking of Virtual hosting of target:- None found"
		
	else:
		print "  "+ " [+]Checking of Virtual hosting of target:- Found. (will save the result in output file)"
		
	csp_parser.main(hostname)	
	
	print '\n', crayons.red('[!]'),  crayons.green('Spidering Target to see if any parameter is Vulnerable to XSS. (will print if any)'), '\n'
	crawler.main(hostname)
	
	print "\n[!] Checking for any s3 buckets \n"
	bucket_finder.main(hostname)
	
	
