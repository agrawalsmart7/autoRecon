import time
import subdomainenum
import port_scanner
import cms_server_frameworks
import anonymous_ftplogin
import fetching_from_wayback
import screenshot_capturer
import optparse
import time
import find_default_files


def run(arg1, arg2, arg3, urls_interesting_files_open):
	subdomainenum.executing_subdomains(arg1, arg2, arg3)
	port_scanner.printingofportscans()
	port_scanner.executing_portscan()
	
	

	cms_server_frameworks.main()
	anonymous_ftplogin.main()
	fetching_from_wayback.main()
	screenshot_capturer.main()
	print "\n\n----------------------------------------------------"
	print   '/[+][+][DONE]. Tryint to get some additional info:- /'
	print   "----------------------------------------------------\n"
	newurl = 'http://'+arg2
	find_default_files.main(newurl,urls_interesting_files_open)
	
	
