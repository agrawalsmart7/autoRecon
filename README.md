# autoRecon

autoRecon is a automation tool which works on Phases which automates the manual process and give results in HTML file. 

**Main domain**

**1.** It will try to find if the domain NS (name server) leaks some Zone transfer file or not.
<br>**2.** It will try to find the Virtual host on that domain. So to give out info about "How many web application   running on single IP". Remember please check if that domain is in scope or not.
<br>**3.** It will try to parse the CSP header (if set). It will store the domains which are set on CS policy. 
<br>`For ex. CSP:- default-src *.test.com www.test1.com test2.com`
<br>then it will parse it and store these domains like `test.com, www.test1.com, test2.com` then it will try to find the JSONp endpoints on those domains through the use of `google.com, ask.com`. (Intentionally for bypassing CSP).
<br>**4** Then it will try to crawl the target and try to find out the vulnerble URL for xss. (If any). Remember it will take one round for crawl. 

**Now on Subdomains.**

**Phase 1**: It will find the sub-domains through the use of the sublist3r.

**Phase 2**: It will find the status code of each sub-domain found by the sublist3r and make separate list of each sub-domain with their respective status code. 

**Phase 3**: In this phase the tool will try to find the CNAME's entries of 404's sub-domains. NOTE: For this Phase, the main objective is to check for the SUBDOMAIN TAKE-OVER Vuln.

**Phase 4**: In this phase, through the use of Multi-threading, this tool will find the Port status running on each Sub-domains. Note: The defined ports are "21, 22, 80, 8080, 443, 8443, 3306, 445". And it will make the two seperate list of URL's which have 21 port open and 80 port open.

**Phase 5**: In this phase the tool will find the *What CMS, Server, Frameworks and versions (if leak) are using in the domain and Sub-domains.

**Phase 6**: In this Phase, if there is any FTP open found by "Phase 4", then it will try to get the Anonymous login.

**Phase 7**: Now in the last phase it will find the URLs in the WayBack machine but whose domain status code is 401, 403. And will Capture screen-shots of way-back URLs.

**Phase 8**:- It will try to find default files for ex. phpinfo.php, htaccess.txt on each and every sub-domain. 
<br>**Phase 9**:- Now lastly it will give you the results in HTML file.


# Usage: 

`C:\>pip install requirements.txt`<br>
`C:\>autoRecon.py -t domainname.com -f <anyfilename.txt> -o <anyfilename.html>`

**Note:** 

-t is for "Target" address and should be in this **domainname.com** format
<br>-f is for "Filename", which is required by this tool. And should be in **.txt** extension.
<br>-o is for "Result out-put HTML file"
# Working Environment

Windows, Linux

# Questions I used to asked myself.

<h2> Goal </h2>

The main aim for this tool is to Automate things, So that you can focus on other things as well.

<h2> Why I use Sub-lister</h2>

I use it because It covers mostly all site which we use to reveal the sub-domains. So, it gives a bunch of Sub domains.

<h2> What is the use of Phase-4 (nmap-scanning)</h2>

Off-course it will find the nmap ports of each sub domains. So if someone finds that there is a port open named FTP, from the bunch of many sub-domains then it has the high probability that it allows anonymously login, and may be some weak passwords as company may not aware about it because of many subdomains. So it alerts you.

<h2> How Screenshots capture?</h2>

This phase uses Selenium, geckodriver for screenshots. Note:- You may see unusal data in the first run in **Linux** because it makes geckodriver in binary form.

# Feedback

I am extremely waiting for your feedback about this tool. 

# Contact


[agrawalsmart7](http://twitter.com/agrawalsmart7)

