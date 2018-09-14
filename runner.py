import time
import subdomainenum
import port_scanner
import cms_server_frameworks
import anonymous_ftplogin
import fetching_from_wayback
import screenshot_capturer
import optparse
import time



def run(arg1, arg2, arg3):
	subdomainenum.executing_subdomains(arg1, arg2, arg3)
	port_scanner.printingofportscans()
	port_scanner.executing_portscan()
	
	

	cms_server_frameworks.main()
	anonymous_ftplogin.main()
	fetching_from_wayback.main()
	screenshot_capturer.main()
	
