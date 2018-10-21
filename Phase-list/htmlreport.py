
import os
from List_of_index import *


def htmlfile(output, hostname):
	try:
		url_for_dns_zone = '<br>'.join(str(s) for s in dns_zone_vul_domains)
		url_for_virtualhost = '<br>'.join(str(x) for x in list_of_virtual_host)
		
		csp_urls = '<br>'.join(str(x) for x in jsonpurls)
		
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
		
		url_default_file = '<br>'.join(str(x) for x in urls_interesting_files_open)
		
		
		

		
		
		wrapper = """

		
		
		

		
		<!DOCTYPE html>

		<html>
		<head>
			<style>
				.div1 {
					
					margin-left: 10px;
					margin-right: 10px;
				}
				.for_headers
				{
					margin-left: 10px;
					margin-top: 5px;
				
				}
				
				.div2{
					border: 1px solid black;
					
				}
				.new_div2{
					border: 1px solid black;
					margin-bottom: 10px;
				
				}
				.div3{
					
				
					border: 1px solid black;
				}
				
			
			
			</style>
		  
		
		  <meta charset=\"utf-8\">
		  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
		  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">
		  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>
		  <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\"></script>
			<title>Results</title>
			<h1 class=\"div1\"><u><center>autoRecon</center></u></h1>
			 <p class=\"div1\" size=\"4\"><center>Target:- %s</center></p></br></br>
			 <br>
			 <h3><u>Gathering Info for Target domain</u></h3><br><br>
			 <p class=\"div1\"><font size=\"4\" color=\"green\"><u color=\"green\" >[+]Vulnerable Zone transfer for Target (If any):-</u></font></p><br>
			 <p class=\"div1\"><font size=\"4\"> %s </font></p>
			  <p class=\"div1\"><font size=\"4\" color=\"green\"><u color=\"green\" >[+]List of Virtual hosts (If any)</u></font></p>
			   <p class=\"div1\"><font size=\"4\"> %s </font></p>
			   <p class=\"div1\"><font size=\"4\" color=\"green\"><u color=\"green\" >[+]JsonWithPadding endpoints for CSP bypass.( If CSP set)</u></font></p>
			   <p class=\"div1\"><font size=\"4\"> %s </font></p>
		</head>
		<body>
		<div class=\"div1\">
		  
		
		<table class=\"div2\" width=\"100%%\" cellpadding = \"4\" border=\"0\" class=\"mar_right\">
		<tbody>
		<tr class=\"div2\">
		<th ><font size=\"3\" width=\"1\" class=\"for_headers\">[ ! ] List of URL's</font>
		<br><br></th>
		<th>
		<font size=\"3\" width=\"1\" class=\"for_headers\">[!] Open Ports on subdomains</font>
		<br><br></th>
		<th>
		<font size=\"3\" width=\"1\" class=\"for_headers\">[!]Web servers list.</font>
		
		<br><br></th>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\" >[+] List of 200 status code subdomains</u><br><br></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\" >[+] List of Open Ports.</u><br><br></font>
		</td>
		<td width=\"33%%\"><font size=\"3\"  color=\"green\"><u color=\"green\" class=\"div1\" >[+]Server/CMS-Versions</u><br><br></font>
		</td>
		
		</tr>
		<tr>
		<td >
		<div  class=\"div1\"><font size=\"4\">%s </font></div>    <!-- forstring = 1-->
		</td>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div>	<!-- forstring = 2-->
		</td>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div>
		</td>
		
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" class=\"div1\" >[-]List of 400 status code subdomains.</u><br><br></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\">[+] List of Open Ports.</u><br><br></font>
		</td>
		<td width=\"33%%\"><font size=\"3\"  color=\"green\"><u color=\"green\" class=\"div1\" >[+]Server/CMS-Versions</u><br><br></font>
		</td>
		</tr>
		<tr>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div><!-- forstring = 3-->
		</td>
		<td>		
			<div  class=\"div1\"><font size=\"4\">%s </font></div>
		</td>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div>	<!-- forstring = 16-->
		</td>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" class=\"div1\" >[-]List of 401 status code subdomains.</u><br><br></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\" >[+] List of Open Ports.</u><br><br></font>
		</td>
		<td width=\"33%%\"><font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\">[+]Server/CMS-Versions</u><br><br></font>
		</td>
		</tr>
		<tr>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div><!-- forstring = 5-->
		</td>
		<td>		
				<div  class=\"div1\"><font size=\"4\">%s </font></div> 	<!-- forstring = 6-->
		</td>
		<td>
				<div  class=\"div1\"><font size=\"4\">%s </font></div> <!-- forstring = 17-->
		</td>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" class=\"div1\" >[-]List of 403 status code subdomains</u><br><br></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" class=\"div1\">[+] List of Open Ports.</u><br><br></font>
		</td>
		<td width=\"33%%\"><font size=\"3\"  color=\"green\"><u color=\"green\" class=\"div1\">[+]Server/CMS-Versions</u><br><br></font>
		
		</td>
		</tr>
		<tr>
		<td>
			<div  class=\"div1\"><font size=\"4\">%s </font></div> <!-- forstring = 7-->
		</td>
		<td>		
			<div  class=\"div1\"><font size=\"4\">%s </font></div><!-- forstring = 8-->
		</td>
		<td>
				<div  class=\"div1\"><font size=\"4\">%s </font></div>	<!-- forstring = 18-->
		</td>
		</tr>
		</tbody>
		  </table>
		<table width=\"100%%\" cellpadding = \"3\" border=\"0\" class=\"div3\" >
		<tbody>
		<tr>
		<td>
		<br><font size=\"3\" color=\"red\"><u color=\"red\" class=\"div1\" >[-]List of 404 status code subdomains.</u><br><br></font>
		</td>
		<td>
		<br><font size=\"3\" color=\"green\"><u color=\"green\" >[+]Cname's of 404 status code subdomains.</u><br><br></font>
		</td>
		<td>
		<br><font size=\"3\" color = \"green\"><u color=\"green\" >[+]List of Open Ports.</u><br><br></font>
		</td>
		<td>
		<br><font size=\"3\" color = \"green\"><u color=\"green\" >[+]Server/CMS-Versions.</u><br><br></font>
		</td>
		</tr>
		<tr>
		<td>
		
		<font size=\"4\">%s </font><!-- forstring = 9-->
		</td>
		<td>
		<font size=\"4\">%s </font><!-- forstring = 10-->
		</td>
		<td>
		 <font size=\"4\">%s </font><!-- forstring = 11-->
		</td>
		<td>
			<font size=\"4\">%s </font>	<!-- forstring = 19-->
		</td>
		</tr>
		</tbody>
		  </table>
		 <div class=\"div2\"> 
		<br><br><h2><center><u > URL's and Screenshots.</u></center></h2>
		<table width=\"100%%\" cellpadding=\"2\">
		
		<br><br><th ><font size=\"3\" class=\"div1\"><u>Uniform Resource Locator.</u></font><br><br></th>
		<br><br><th> <font size=\"4\" class=\"div1\"><u>Web-Screenshots.</u></font><br><br></th>
		 
		<tr>
		<td ><div  class=\"div1\"><font size=\"4\">%s </font></div> </td>
		<td ><div  class=\"div1\"><font size=\"4\">%s </font></div> </td>
		</tr>	<!-- forstring = 13-->
		<!-- forstring = 14-->
		
		</table>
		 </div>
		<div class=\"new_div2\">
		<br><br><h2><center><u>Additional Info</u></center></h2>
		<p><font size=\"4\" class=\"div1\" ><u><b>List of the interesting URL's. (if any) </b></u></font></p>
		<div  class=\"div1\"><font size=\"4\">%s </font></div>
		</div>
		</body>
		</html>"""
		
		get_cwd = os.getcwd()
		hrml_report = os.chdir('results')
		
		file = open(output, 'w')
		file.write(wrapper % (hostname, url_for_dns_zone, url_for_virtualhost , csp_urls, url_200_list, open_ports_200, info_200_urls, url_400_list , open_ports_400,info_400_urls, url_401list ,open_ports_401 ,info_401_urls, url_403list,open_ports_403 ,info_403_urls, url_404list , url_404_cname, open_ports_404, info_404_urls ,urls_from_wayback401 ,urls_from_wayback403, url_default_file))
		
		file.close()
		os.chdir(get_cwd)
	except Exception as e:
		print e
		
		
		