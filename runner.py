import subdomainenum
import port_scanner
import cms_server_frameworks
import anonymous_ftplogin
import fetching_from_wayback
import screenshot_capturer
import find_default_files
import dnshistory
import parse8080

def run(arg1, arg2, arg3, urls_interesting_files_open):

	
	
	subdomainenum.executing_subdomains(arg1, arg2, arg3)
	port_scanner.printingofportscans()
	port_scanner.executing_portscan()
	
	cms_server_frameworks.main()
	anonymous_ftplogin.main()
	fetching_from_wayback.main()
	screenshot_capturer.main()
	print "\n\n---------------------------------------------------"
	print    '|[+][DONE]. Trying to get some additional info:- |'
	print     "---------------------------------------------------\n"
	newurl = 'http://'+arg2
	
	
	find_default_files.main(urls_interesting_files_open)
	
	print "\n [+]List of some interesting URL's (if so) \n"
	for x in urls_interesting_files_open:
		print "   ", x.strip('\n')
	
	print '\n [+] Trying to find the DNS history whose server is Cloudflare \n'
	dnshistory.main()
	
	print "\n[!] Parsing 8080 port for Info \n"
	parse8080.parse8080()
	
	
	
	
	
	
	
	
	
	
	
	
	