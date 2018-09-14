
import os
from List_of_index import *


def htmlfile(output):
	try:
		forstring = '<br>'.join(str(key) for key, value in getvalue200.iteritems())
		forstring2 = '<br>'.join((str(getvalue200[key][0]).strip('[]')) for key, value in getvalue200.iteritems())
		forstring3 ='<br>'.join(str(key) for key, value in dict400.iteritems())
		forstring4= '<br>'.join((str(value).strip('[]')) for key, value in dict400.iteritems())
		forstring5='<br>'.join(str(key) for key, value in dict401.iteritems())
		forstring6='<br>'.join((str(value).strip('[]')) for key, value in dict401.iteritems())
		forstring7='<br>'.join(str(key) for key, value in dict403.iteritems())
		forstring8= '<br>'.join((str(value).strip('[]')) for key, value in dict403.iteritems())
		forstring9='<br>'.join(str(key) for key, value in dictcname.iteritems())
		forstring10='<br>'.join((str(value).strip("\'\'\[\]")) for key, value in dictcname.iteritems())
		forstring11='<br>'.join((str(value).strip('[]')) for key, value in dict404.iteritems())
		forstring13 = ''.join (str(key) for key, value in waybackurls401.iteritems())
		forstring14 = ''.join (str(key) for key, value in waybackurls403.iteritems())
		forstring15 = '<br>'.join(((str(getvalue200[key][1]).translate(None, "[]''")) for key, value in getvalue200.iteritems()))
		forstring16 = '<br>'.join(((str(getvalue400[key][1]).translate(None, "[]''")) for key, value in getvalue400.iteritems()))
		forstring17= '<br>'.join(((str(getvalue401[key][1]).translate(None, "[]''")) for key, value in getvalue401.iteritems()))
		forstring18= '<br>'.join(((str(getvalue403[key][1]).translate(None, "[]''")) for key, value in getvalue403.iteritems()))
		forstring19= '<br>'.join(((str(getvalue404[key][1]).translate(None, "[]''")) for key, value in getvalue404.iteritems()))
		
		wrapper = """

		<style>body {
			background-color: #C0C0C0;
		}
		</style>
		<!DOCTYPE html>

		<html>
		<head>
		<h1><center><u>HTML report.</u></center></h1>
		</head>
		<br><br>
		<table width=\"100%%\" cellpadding = \"4\" border=\"0\">
		<tbody>
		<tr>
		<th><u>[!]List of URL's
		</u></th>
		<th>
		<u>[!] Open Ports on subdomains
		</u></th>
		<th>
		<u>[!]Web servers list.
		
		</u></th>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+] List of 200 status code subdomains</u></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+] List of Open Ports.</u></font>
		</td>
		<td width=\"33%%\"><font color=\"green\"><u color=\"green\" >[+]Server/CMS-Versions</u></font>
		</td>
		
		</tr>
		<tr>
		<td>
		%s                   <!-- forstring = 1-->
		</td>
		<td>
		%s		<!-- forstring = 2-->
		</td>
		<td>
		%s		<!-- forstring = 15-->
		</td>
		
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" >[-]List of 400 status code subdomains.</u></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+] List of Open Ports.</u></font>
		</td>
		<td width=\"33%%\"><font color=\"green\"><u color=\"green\" >[+]Server/CMS-Versions</u></font>
		</td>
		</tr>
		<tr>
		<td>
		%s <!-- forstring = 3-->
		</td>
		<td>		
		%s		<!-- forstring = 4-->
		</td>
		<td>
		%s		<!-- forstring = 16-->
		</td>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" >[-]List of 401 status code subdomains.</u></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+] List of Open Ports.</u></font>
		</td>
		<td width=\"33%%\"><font color=\"green\"><u color=\"green\" >[+]Server/CMS-Versions</u></font>
		</td>
		</tr>
		<tr>
		<td>
		%s  <!-- forstring = 5-->
		</td>
		<td>		
		%s		<!-- forstring = 6-->
		</td>
		<td>
		%s		<!-- forstring = 17-->
		</td>
		</tr>
		<tr>
		<td width=\"33%%\">
		<font size=\"3\" color=\"red\"><u color=\"red\" >[-]List of 403 status code subdomains</u></font>
		</td>
		<td width=\"33%%\">
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+] List of Open Ports.</u></font>
		</td>
		<td width=\"33%%\"><font color=\"green\"><u color=\"green\" >[+]Server/CMS-Versions</u></font>
		</td>
		</tr>
		<tr>
		<td>
		%s <!-- forstring = 7-->
		</td>
		<td>		
		%s		<!-- forstring = 8-->
		</td>
		<td>
		%s		<!-- forstring = 18-->
		</td>
		</tr>
		</tbody>
		  </table>
		<table width=\"100%%\" cellpadding = \"3\" border=\"0\">
		<tbody>
		<tr>
		<td>
		<font size=\"3\" color=\"red\"><u color=\"red\" >[-]List of 404 status code subdomains.</u></font>
		</td>
		<td>
		<font size=\"3\" color=\"green\"><u color=\"green\" >[+]Cname's of 404 status code subdomains.</u></font>
		</td>
		<td>
		<font size=\"3\" color = \"green\"><u color=\"green\" >[+]List of Open Ports.</u></font>
		</td>
		<td>
		<font size=\"3\" color = \"green\"><u color=\"green\" >[+]Server/CMS-Versions.</u></font>
		</td>
		</tr>
		<tr>
		<td>
		%s<!-- forstring = 9-->
		</td>
		<td>
		%s<!-- forstring = 10-->
		</td>
		<td>
		%s <!-- forstring = 11-->
		</td>
		<td>
		%s		<!-- forstring = 19-->
		</td>
		</tr>
		</tbody>
		  </table>
		<h2><center><u> URL's and Screenshots.</u></center></h2>
		<table width=\"100%%\" cellpadding=\"2\">
		
		<br><br><th font size="4"><u>Uniform Resource Locator.</u></th>
		<br><br><th font size="4"><u>Web-Screenshots.</u></th>
		%s <!-- forstring = 13-->
		%s<!-- forstring = 14-->
		
		</table>
		</html>"""
		
		get_cwd = os.getcwd()
		hrml_report = os.chdir('results')
		
		file = open(output, 'w')
		file.write(wrapper % (forstring, forstring2, forstring15, forstring3 , forstring4,forstring16, forstring5 ,forstring6 ,forstring17, forstring7,forstring8 ,forstring18,forstring9 ,forstring10, forstring11, forstring19 ,forstring13 ,forstring14))
		
		file.close()
		os.chdir(get_cwd)
	except Exception as e:
		print e
		
		
		