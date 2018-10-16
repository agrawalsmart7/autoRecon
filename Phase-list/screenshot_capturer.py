from List_of_index import *
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException


def drivers():
	try:
		
		
		file = os.getcwd()
		location = file+'/'+'geckodriver.exe'
		
		os.environ['DIR'] = location
		CHROMEDRIVER_PATH = location

		firefox_options = Options()  
		firefox_options .add_argument("-headless")  
		driver = webdriver.Firefox(executable_path=CHROMEDRIVER_PATH, firefox_options = firefox_options ) 
		
		
		
		return driver
	except Exception as e:
		print e
	
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
		
		

def executing_functions():
	driver = drivers()
	get_cwd = os.getcwd()
	
	new_dir = os.chdir('screenshots')
	for x in webarchive_urls401:
		driver.set_page_load_timeout(5)
		drivers_func(x, waybackurls401, driver)
	
	for y in webarchive_urls403:
		driver.set_page_load_timeout(5)
		drivers_func(y, waybackurls403, driver)
		
	driver.close()		
	os.chdir(get_cwd)
def main():
	executing_functions()
