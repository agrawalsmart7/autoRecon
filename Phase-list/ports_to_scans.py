import threading

def formate(newurl1, schemess, connCheck):
	newurl = newurl1.replace('http://', '')
	portss = 21, 22, 80, 8080, 443, 8443, 3306, 445	
	th1 = threading.Thread(target=connCheck,  args= (newurl, schemess, 21, ''))
	th2 = threading.Thread(target=connCheck,  args=( newurl, schemess, 22, ''))
	th3 = threading.Thread(target=connCheck,  args= (newurl, schemess,80, ''))
	th4 = threading.Thread(target=connCheck,  args=(newurl, schemess,8080, ''))
	th5 = threading.Thread(target=connCheck,  args= (newurl, schemess,443, ''))
	th6 = threading.Thread(target=connCheck,  args= (newurl, schemess,8443, ''))
	th7 = threading.Thread(target=connCheck,  args= (newurl, schemess,3306, ''))
	th8 = threading.Thread(target=connCheck,  args= (newurl, schemess,445, ''))
	
	print "\n ----------------------", "\n"
	print "\tList of open ports:-"
	
	th1.start()
	th2.start()
	th3.start()
	th4.start()
	th5.start()
	th6.start()
	th7.start()
	th8.start()
	th8.join()