from List_of_index import *
import os
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import sys
from sys import platform


def windows_func():
	try:
		
		
		file = os.getcwd()
		location = file+'/'+'geckodriver.exe'
		
		os.environ['DIR'] = location
		geckodriver = location
		
		firefox_options = Options()  
		firefox_options.add_argument("-headless")  
		driver = webdriver.Firefox(executable_path=geckodriver, firefox_options = firefox_options ) 
		return driver

		
	except Exception as e:
		print e
		
def get_geckodriver(version):
	try:
	
		os.system("wget https://github.com/mozilla/geckodriver/releases/download/"+str(version)+"/geckodriver-"+str(version)+"-linux64.tar.gz ; tar xvzf geckodriver-"+str(version)+"-linux64.tar.gz ; chmod +x geckodriver ;") 
	
	except OSError as e:
		print e		
		
def check_selenium_version():
	

	if selenium.__version__  >= 3.4 and selenium.__version__ < 3.5:
		get_geckodriver('v0.18.0')
		
		
	elif selenium.__version__  >= 3.5:
		get_geckodriver('v0.20.1')
		
def linux_func2():

	file = os.getcwd()
	location = file+'/'+'geckodriver'
	firefox_options = Options()  
	firefox_options.add_argument("-headless")  
	driver = webdriver.Firefox(executable_path=location, firefox_options = firefox_options ) 
	return driver

		
def drivers_func(x, waybackurls, driver):
	
	
	
	print "\t[+]" + x
	try:
		
		driver.get(x)
		
		imgfilename  = x.split('/web/')[-1] 
		newfile= imgfilename.replace('/', '.') +'.png'
		
		driver.save_screenshot(newfile)
		newloc = os.getcwd()+'/{0}'.format(newfile)
		
		
		value = "<td><img src= file:///"+newloc + " width='20%' height= '25%'></td>".format(newfile)
		key = "<tr><td width=\"50%\">{0}</td><td width=\"50%\"><img src= file:///{1} width='30%' height= '20%'><br><a href=\"{2}\">URL</a></td></tr>".format(x,newloc ,x)
		
		
		waybackurls[key] = value
	except Exception as e:
		print "\t [-]Timeout of this URL:- ", x
		
		

def executing_functions(driver):
	get_cwd = os.getcwd()
	new_dir = os.chdir('screenshots')
	for x in webarchive_urls401:
		driver.set_page_load_timeout(20)
		drivers_func(x, waybackurls401, driver)
	
	for y in webarchive_urls403:
		driver.set_page_load_timeout(20)
		drivers_func(y, waybackurls403, driver)
		
	driver.close()		
	os.chdir(get_cwd)
	
def check_os():

	
	if sys.platform == 'win32':
	
		driver = windows_func()
		executing_functions(driver)
		
	elif sys.platform == 'linux2':
		try:
			
		
			driver = linux_func2()
			executing_functions(driver)
		except:
			check_selenium_version()
			driver = linux_func2()
			executing_functions(driver)
	
def main():
	
	urls_check = [webarchive_urls401, webarchive_urls403]
	
	for x in urls_check:
		
		if not x:
			None
		else:
			
			check_os()

	

