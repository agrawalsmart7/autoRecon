import ftplib
from ftplib import FTP
from List_of_index import ftpurls, ftpanonymous
import json_output


def printing_of_ftp_login():
	
	print "\n...............................................................................................\n"
	print "\n\n                                                 [PHASE: 6]: Starts below                                                \n\n"
	print "[!]Executing anonymous login one by one on Subdomains which have FTP port open. If any.\n"
	
def ftp_login_check(x):
	x = x.replace('http://', '')
	
	try:
		 
		s =ftplib.FTP(host=x, user='', acct='', timeout=6)
		ss =  s.login()	
		if ss:
			print "\t Host : "+ str(x) + "\n"
			print "\t [+]Vulnerable FTP allows anonymous login. \n"
			value = "[+]Vulnerable FTP allows anonymous login. "
			
			ftpanonymous[x] = 'FTP Vulnerable'
	
	except ftplib.all_errors as e:
		print "Host : "+ str(x)
		print "[-]Login Incorrect. Not allowing anonymous login.\n"	
		
def executing_ftp_login():
	
	for x in ftpurls:
		ftp_login_check(x)	
		

def main():
	printing_of_ftp_login()
	executing_ftp_login()
	json_output.json_output('ftp_anonymous', ftpanonymous)