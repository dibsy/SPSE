# SPSE EXERCISES SOLUTIONS
## SPSE - Securitytube Python Scripting Expert Course Problems Solution
#### The SecurityTube Python Scripting Expert (SPSE) is an online certification which will help you gain mastery over Python scripting and its application to problems in computer and network security. This course is ideal for penetration testers, security enthusiasts and network administrators who want to learn to automate tasks or go beyond just using ready made tools. We will be covering topics in system security, network security, attacking web applications and services, exploitation techniques, malware and binary analysis and task automation.

### Module 1 : Python Language Essentials

### Module 2 : System Programming

1. Read Var/log/messages and find all the logs in it which pertain to usb and print them out seperately - Done 
2. Create a Program which can recursively traverse directories and Print the file listing in the a hirerachial way - Done

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

1. Create a simple Echo Server to handle 1 client
   Create a Multi-Threaded Echo Server
   Create a Multi-Process Echo Server
   Create a Non-Blocking Multiplexed Echo Server using Select()

2. Create a Packet Sniffer using Raw Sockets which can parse TCP packets - parse individuals fields

3. Create a sniffer which uses a fliter to only print details of an HTTP packet packet (TCP, Port 80)- Also dump the data

4. Create a Packet Sniffer with Scapy for HTTP protocol and print out the HTTP Headers and the data in GET/POST

5. Create a WiFi Sniffer and print out the unique SSIDs of the WiFi networks in your vicinity

6. Create ARP Request packets for the local subnet. Send and Receive Responses and get results and publish.Find out how to get the local subnet automatically. 

7. Create a DNS Poisoning tool similar to Dnsspoof using scapy

8. Create a ARP MITM tool using scapy

9. Create TCP SNY Scanner using Scapy

10. Explore how to create a Fuzzer with Scapy

11. Create a DNS Fuzzer with Scapy and try it against DNSspoof
  
### Module 4 : Attacking Web Applications

1. If you try and download a very large file, then how do you monitor the progress?Research on urllib.urlretrieve() to solve this problem

2. Urlencode() does a bad job in handling special characters in the URL. Research on .quote() and .quote_plus() and illustrate how they can help

3. Read the documentation of BeautifulSoup 4 and find other ways to iterate through tags and get to the juicy information - Done

4. In the example shown we did not try and modify the hidden fields. Try to see how you can do it and send arbitrary data

5. Install a vulnerable web application such as DVWA, OWASP Web Goat or other - Done

6. Use mechanize to try SQL Injection on form fields and deduce which fields are vulnerable to SQL Injection - Done

7. Explore the concept of mechanize.CookieJar

8. Attack on Web Service

9. Investigate on how you can use Proxy support with: BeautofulSoup,urllib,mechanize

10. Create a Multi-Threaded Web Spider which takes a website and depth of spidering as input ,download the HTML files only,Inserts the HTML into a MySQL Database,Design the Schema,It also parses the Forms on each page,inserts into DB with details of Form fields

11. For each of the OWASP Top 10 create Python scripts which can automate the testing of the vulnerability 

### Module 5 : Exploitation Techniques

1. Using Immunity Debugger Python module list all the running process and show them in a new window
2. Write the list of processess in a CSV file.The first row should be the table columns name

### Module 6 : Reverse Engineering

1. Take a DLL name as input and check if a given PE imports it and print the list of imports  

2. Create a simple program which can disassemble the first 200 bytes of executable code 

3. Create simple shellcode for a windows bind shell and then use pydasm to disassemble it

4. Install Pydbg to run on Python 2.7.x

5. Modify the code to take a file loca1on as input and then automa1cally runs to  file

6. Modify the program to include full crash dump details. Explore how you can get all the info using the u1ls module  

7. For both send / recv calls read the arguments from the stack when the breakpoint is hit and print the contents out in an intelligible way coherent with the API documentation

8. Create API monitors for the following: – Registry writes to “run on login/boot” – Opening / Wri1ng of files – Send / Recv on network. Once you create the above framework, get a malware or program sample and test against it 

9. Setup Cuckoo Box

10. Analyze a program with it and log – API calls – Files it reads / writes – Host it communicates with 

### Module 7: Automation In Python

1. SSH Automation with Paramiko

2. SSH Dictionary Attack with Paramiko

3. SFTP With Paramiko

### Module 8: Further Study and Projects

1. Create a Bot which can use Twitter as C&C.•It will scan the public tweets using a #tag and a command will be inserted in the Tweet e.g. Tweet. `#exec129834 ipconfig –a` .The bot will now execute “ipconfig –a” and paste the results in Pastebin

2. Create a automated Email Parser – when email is received in your account, this script will automatically be triggered, it will then separate the attachments, store them in a directly and upload them to online virus scan sites.It will then forward the email to you if the online scans give a green signal!!

3. Code a program which can read an EXE and dump interesting information such as import/exports, disassembly, strings etc.Basically a powerful Level 1 binary analysis tool before you put the EXE into a debugger


### Module 9: Exam pattern And Mock Exam

1. We have setup a web server at http://XXX. Code a Python Script to scrape the HTML and list all the forms and respective fields,try SQL Injection on each of the fields using a database of possibilities from a given file. Submit the script and the form fields returning +ve for SQL Injection

2. Create a Python script which allows you to inspect the “bind” network call and logs the port and IP address used. Can be standalone or a Plugin.Works on Windows

3. Write a simple web crawler which fetch the robots.txt file of a website.Run your crawler on the top 1000 sites a ranked by Alexa.Report on the top 40 directory names which are disallowed for robots
 

