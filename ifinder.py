#!/usr/bin/python
import urllib.request
import pyfiglet																																																																		
import subprocess as sp
import socket
from urllib.parse import urlparse

banner = pyfiglet.figlet_format("ifinder")
print(banner)

name = input("Enter the file name ")
file = open(name, "r")
print("\n Opening file for reading.",end = "\r")
print("Please be patient ")
Lines = file.readlines()
count = 0
file_create = sp.getoutput ("touch Ip-list.txt && chmod +x Ip-list.txt")
file_create_1 = sp.getoutput ("touch Ip-list-with-domain.txt && chmod +x Ip-list-with-domain.txt")
for line in Lines:
    count += 1
    domain = urlparse(line.strip()).netloc
    ip = socket.gethostbyname(domain)
    ip_add = sp.getoutput("echo {} >> Ip-list.txt ".format(ip))
    ip_add = sp.getoutput("echo {} - {} >> Ip-list-with-domain.txt ".format(domain, ip))
    print("IP for {} is {} ".format(domain, ip))
    sort = sp.getoutput("sort Ip-list.txt | uniq | tee Ip-list-uniq.txt ")


print("\n\nYour IPs listed without domain names on Ip-list.txt")    	
print("Your IPs with domain names listed on Ip-list-with-domain.txt")    	
print("Your Uniq IPs  listed on Ip-list-uniq.txt")    	
