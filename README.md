# ifinder
 ifinderis simple python tool for finding IP address for bunch of live subdomains.Generally subdomain enumeration tools (Eg. sublist3r) provide a list that consists of both Live and down subdomains. Then user separate the live domains.Hence the user time will be wasted to separate the unique sub domains alone (Based on IP).  So we have introduced this simple ifinder tool to get the ip address for subdomains. ifinder read the subdomain list which is provided by subdomain enumeration tool and gives the Ip address list separately for bug bounty.
 
**Pre requisites**

subprocess

socket

urllib.parse

**Installation**

> pip install subprocess

> pip install socket

> pip install urllib.parse

To run the file

>git clone https://github.com/virtuvil/ifinder

Your URL has to be given above. Now navigate to qping directory

>cd ifinder

Now you can run qping

>python3 ip-finder.py

