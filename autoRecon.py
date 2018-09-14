import optparse
import time
import sys
import os 
get_cwd = os.getcwd()
sys.path.insert(0, get_cwd+'/Phase-list/')

import runner
from List_of_index import *
import htmlreport



start = time.time()
parser = optparse.OptionParser() 
parser.add_option("-t","--Host", dest="host", help="Please provide the target")
parser.add_option("-f","--file", dest="file", help="Please provide the filename")
parser.add_option("-o", "--Output", dest="result", help="")


options, args = parser.parse_args() 
hostname = options.host
filename = options.file
output = options.result



def logo():
	outputt = """

	                    __             ___ _                          	 
	   ___ _   __  __  / /_  ____     / -- /  _ _    _ _   ___ _     _  _
	  / __  / / / / / / __/ / __  \  /_ _ / / _ _/ /  _ /  / __  \  /  _   /
 	 / /_/ / / /_/ / / /_  / /__/ / / \    /      / /_   / /__/ / / /  / /
	 \__,_/  \___ /  \__/  \ ___ / /   \   \ _ _  \ _ /  \ ___ / /_/  /_/
	 
	 # Code written by @agrawalsmart7
	 
	   
	"""
	print outputt

def error():
	error  = '\n Usage: autoRecon.py -t domain.com -f yourfilename.txt -o output.html'
	print error

	
def timew():
	print "Total time taken:- ", time.time()-start, 'seconds'
	

def main (output):
	
	# the below functions are for phase1 and phase2
	
	
	runner.run(newurllist, hostname, filename)
	
	htmlreport.htmlfile(output)
	
	timew()
	
	
if __name__ == '__main__':
	
	try:
		
		if hostname and filename and output :

			logo()
			main(output)
			
		else:
			error()	
			
			
	except Exception as e:
		print e
