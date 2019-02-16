from json2html import *
from List_of_index import *
import json
import os
from HTMLParser import HTMLParser


 

def htmlfile(output, hostname):
	h = HTMLParser()
	os.chdir('results')
	url_for_virtualhost = '<br>'.join(str(x) for x in list_of_virtual_host)
	csp_urls = '<br>'.join(str(x) for x in jsonpurls)
	xss_urls = '<br>'.join(str(x) for x in vulnerable)
	json1 = json.dumps(json_dict, indent=2, sort_keys=True)
	
	bucket_urls = '<br>'.join(str(x) for x in buckets)


	urls_from_wayback401 = ''.join (str(key) for key, value in waybackurls401.iteritems())
	urls_from_wayback403 = ''.join (str(key) for key, value in waybackurls403.iteritems())

	table_attributes = 'id="domain"'
	html_code = json2html.convert(json = json1, table_attributes = table_attributes)
	newhtml_code = h.unescape(html_code)
	fileopen = open(output, 'w')
	fileopen.write("""<!doctype html>
						<html lang="en">
						<head>
						<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
						<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css" />
						<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js">
						<link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.bundle.min.js">

						<style>
						div {
						margin-left: 30px;
						}
						#domain {
						font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
						border-collapse: collapse;
						width: 100%%;
						}

						#domain td, #domain th {
						border: 1px solid #ddd;
						padding: 8px;
						}

						#domain tr:nth-child(even){background-color: #f2f2f2;}


						</style>
						<u><title>AutoRecon | Results</title></u>
						<center><u><h2>Autorecon Results </h2></u><br>
						<h5>TARGET:- %s </h5></center>
						<br><br>
						<div class="container">
						<u><font color="green"><h4> Virtual hosting found(if any)</h4></font>
						%s<br><br>
						<font color="red"><h4>URL's which have jsonP endppoint open(if any)</h4></font>
						%s
						<br><br>
						<font color="red"><h4 >XSS Vulnerable Urls Found(if any)</u></h4></font>
						%s
						<br><br>
						<font color="red"><h4 >S3 Buckets found(if any)</u></h4></font>
						%s
						<br><br>
						
						<h3><font color="green">Information found on subdomains below:- </h3><br></font></u>

						</head>
						<body>
						<a href="https://github.com/agrawalsmart7/autorecon/" class="github-corner" target="_blank" title="Star me on Github">
						<svg width="80px" height="80px" viewBox="0 0 250 250" style="fill:#4db6ac; color:#fff; position: absolute; top: 0; border: 0; right: 0;">
						<path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
						<path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
						<path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>
						</svg>
						</a>""" % (hostname, url_for_virtualhost, csp_urls, xss_urls, bucket_urls))
	fileopen.write(newhtml_code)
	fileopen.write("""
					<br><br>
					<font color="green"><h4 >List of screenshots which are found in way-back machine</u></h4></font>
					%s	
					%s
					<br><br>""" %(urls_from_wayback401, urls_from_wayback403))
	fileopen.write('</div></body></html>')
	
	return file