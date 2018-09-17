from List_of_index import *
import dns_zone_testing
import find_default_files
import virtual_host_testing

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