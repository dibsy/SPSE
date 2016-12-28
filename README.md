# SPSE
## SPSE - Securitytube Python Scripting Expert Course Problems Solution
#### The SecurityTube Python Scripting Expert (SPSE) is an online certification which will help you gain mastery over Python scripting and its application to problems in computer and network security. This course is ideal for penetration testers, security enthusiasts and network administrators who want to learn to automate tasks or go beyond just using ready made tools. We will be covering topics in system security, network security, attacking web applications and services, exploitation techniques, malware and binary analysis and task automation.

### Module 1 : Python Language Essentials

### Module 2 : System Programming


1. Read Var/log/messages and find all the logs in it which pertain to usb and print them out seperately - Done 
2. Create a Program which can recursively traverse directories and Print the file
listing in the a hirerachial way - Done

A
- - - - a.txt
- - - - b.txt
- - - - B
- - - - - - - - c.out

3. for any given filename list out all the stats releated to the file size , creation time , path , etc - Done

4. Based on the knowledge you have gained in the network programming module, create a multi-threaded port scanner in Python which uses SYN Scanning

5. Create a list of FTP sites Create a WorkerThread and Queue which can login to these sites and list the root directory and exit use 5 threads for this job and 10 FTP sites - Done

6. There is a locking mechanism available in the Thread class which you can use to lock resources for dedicated use

7. Explore the multiprocessing module in Python.How does it leverage multi-core setups? Program the TCP SYN scanner using multiprocessing

8. Create a TCP server which listens to a port Implement signals to ensure it automatically shuts down after a pre-configured duration, which is given via command line e.g. tcp-server –s 100 shutdown after listening to port for 100 seconds

### Module 3: Network Security

1.Create a simple Echo Server to handle 1 client
    Create a Multi-Threaded Echo Server
    Create a Multi-Process Echo Server
    Create a Non-Blocking Multiplexed Echo Server using Select()

### Module 4 : Attacking Web Applications

1. If you try and download a very large file, then how do you monitor the progress?
Research on urllib.urlretrieve() to solve this problem - Done

2. Urlencode() does a bad job in handling special characters in the URL
Research on .quote() and .quote_plus() and illustrate how they can help

3. Read the documentation of BeautifulSoup 4 and find other ways to iterate through tags and get to the juicy information - Done

4. In the example shown we did not try and modify the hidden fields. Try to see how you can do it and send arbitrary data

5. Install a vulnerable web application such as DVWA, OWASP Web Goat or other - Done

6. Use mechanize to try SQL Injection on form fields and deduce which fields are vulnerable to SQL Injection - Done

7. Explore the concept of mechanize.CookieJar

8. Attack on Web Service

9. Investigate on how you can use Proxy support with:
–BeautofulSoup
–urllib
–mechanize

10.Create a Multi-Threaded Web Spider which
–takes a website and depth of spidering as input
–download the HTML files only
–Inserts the HTML into a MySQL Database
•Design the Schema
–It also parses the Forms on each page
•inserts into DB with details of Form fields

11. For each of the OWASP Top 10 create Python scripts which can automate the testing of the vulnerability 

### Module 5 : Exploitation Techniques

### Module 6 : Reverse Engineering

### Module 7: Automation In Python


### Module 8: Further Study and Projects

•Create a Bot which can use Twitter as C&C
•It will scan the public tweets using a #tag and a command will be inserted in the Tweet
•e.g. Tweet
`#exec129834 ipconfig –a`
The bot will now execute “ipconfig –a” and paste the results in Pastebin



 
•Create a automated Email Parser – when email is received in your account, this script 
will automatically be triggered, it will then separate the attachments, store them in a 
directly and upload them to online virus scan sites.
•It will then forward the email to you if the online scans give a green signal!!




•Code a program which can read an EXE and dump interesting information such as 
import/exports, disassembly, strings etc.
•Basically a powerful Level 1 binary analysis tool before you put the EXE into a debugger


### Module 9: Exam pattern And Mock Exam

We have setup a web server at http://XXX
Code a Python Script to scrape the HTML and
–list all the forms and respective fields
–try SQL Injection on each of the fields using a database of possibilities from a given file
Submit the script and the form fields returning +ve for SQL Injection



Create a Python script which allows you to inspect the “bind” network call and logs the 
port and IP address used
–Can be standalone or a Plugin
–Works on Windows



Write a simple web crawler which fetch the robots.txt file of a website.Run your crawler on the top 1000 sites a ranked by Alexa.Report on the top 40 directory names which are disallowed for robots


