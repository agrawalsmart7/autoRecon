
import os
from List_of_index import *


def htmlfile(output):
	try:
		url_200_list = '<br>'.join(str(key) for key, value in getvalue200.iteritems())
		open_ports_200 = '<br>'.join((str(getvalue200[key][0]).strip('[]')) for key, value in getvalue200.iteritems())
		info_200_urls = '<br>'.join(((str(getvalue200[key][1]).translate(None, "[]''")) for key, value in getvalue200.iteritems()))
		
		url_400_list ='<br>'.join(str(key) for key, value in dict400.iteritems())
		open_ports_400= '<br>'.join((str(value).strip('[]')) for key, value in dict400.iteritems())
		info_400_urls = '<br>'.join(((str(getvalue400[key][1]).translate(None, "[]''")) for key, value in getvalue400.iteritems()))
		
		url_401list='<br>'.join(str(key) for key, value in dict401.iteritems())
		open_ports_401='<br>'.join((str(value).strip('[]')) for key, value in dict401.iteritems())
		info_401_urls= '<br>'.join(((str(getvalue401[key][1]).translate(None, "[]''")) for key, value in getvalue401.iteritems()))
		
		url_403list='<br>'.join(str(key) for key, value in dict403.iteritems())
		open_ports_403= '<br>'.join((str(value).strip('[]')) for key, value in dict403.iteritems())
		info_403_urls= '<br>'.join(((str(getvalue403[key][1]).translate(None, "[]''")) for key, value in getvalue403.iteritems()))
				
		url_404list='<br>'.join(str(key) for key, value in dictcname.iteritems())
		url_404_cname='<br>'.join((str(value).strip("\'\'\[\]")) for key, value in dictcname.iteritems())
		open_ports_404='<br>'.join((str(value).strip('[]')) for key, value in dict404.iteritems())
		info_404_urls= '<br>'.join(((str(getvalue404[key][1]).translate(None, "[]''")) for key, value in getvalue404.iteritems()))
		
		urls_from_wayback401 = ''.join (str(key) for key, value in waybackurls401.iteritems())
		urls_from_wayback403 = ''.join (str(key) for key, value in waybackurls403.iteritems())
		
		
		

		
		
		wrapper = """

		<!DOCTYPE html>
		<html lang="en">
		<head>
		  <title>Bootstrap Example</title>
		  <meta charset="utf-8">
		  <meta name="viewport" content="width=device-width, initial-scale=1">
		  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>

		<div class="container-fluid">
		  <h1>Hello World!</h1>
		  <p>Resize the browser window to see the effect.</p>
		  <p>The columns will automatically stack on top of each other when the screen is less than 768px wide.</p>
		  <div class="row">
			<div class="col-sm-4" style="background-color:lavender;">[!]List of 200 urls<br><br></div><br>
			<div>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]OpenPorts of 200 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]CMS/WebServer/Frameworks<br><br>%s</div>
			
		  </div>
		   <div class="row">
			<div class="col-sm-4" style="background-color:lavender;">[!]List of 400 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]OpenPorts of 400 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]CMS/WebServer/Frameworks<br><br>%s</div>
			
			
			
		  </div>
		   <div class="row">
			<div class="col-sm-4" style="background-color:lavender;">[!]List of 401 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]OpenPorts of 401 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]CMS/WebServer/Frameworks<br><br>%s</div>
			
		  </div>
		   <div class="row">
			<div class="col-sm-4" style="background-color:lavender;">[!]List of 403 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]OpenPorts of 403 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]CMS/WebServer/Frameworks<br><br>%s</div>
			
			
		  </div>
		   <div class="row">
			<div class="col-sm-2" style="background-color:lavender;">[!]List of 404 urls<br><br>%s</div>
			<div class="col-sm-4" style="background-color:lavenderblush;">[!]CnameEntries 404 urls <br><br>%s</div>
			<div class="col-sm-3" style="background-color:lavender;">[!]OpenPorts of 404 urls<br><br>%s</div>
			<div class="col-sm-3" style="background-color:lavenderblush;">[!]CMS/WebServer/Frameworks<br><br>%s</div>
		  </div>
		</div>
			
		
		<h2><center><u> URL's and Screenshots.</u></center></h2>
		<table width=\"100%%\" cellpadding=\"2\">
		
		<br><br><th font size="4"><u>Uniform Resource Locator.</u></th>
		<br><br><th font size="4"><u>Web-Screenshots.</u></th>
		%s <!-- forstring = 13-->
		%s<!-- forstring = 14-->
		
		</table>
		</body>
		</html>
		"""
		
		get_cwd = os.getcwd()
		hrml_report = os.chdir('results')
		
		file = open(output, 'w')
		file.write(wrapper % (url_200_list, open_ports_200, info_200_urls, url_400_list , open_ports_400,info_400_urls, url_401list ,open_ports_401 ,info_401_urls, url_403list,open_ports_403 ,info_403_urls, url_404list , url_404_cname, open_ports_404, info_404_urls ,urls_from_wayback401 ,urls_from_wayback403))
		
		file.close()
		os.chdir(get_cwd)
	except Exception as e:
		print e
		
		
		