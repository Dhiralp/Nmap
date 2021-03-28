# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:49:18 2021

@author: Dhiral
"""

import nmap
import sys
import os
import time

nm_scan = nmap.PortScanner()
print("Running....\n")

#host = '172.217.20.14'
host = '172.217.164.78'
"""
If your want to use host from argument use below command

host = sys.argv[1]
"""
nm_scanner = nm_scan.scan(host,'80',arguments='-O')

host_status = "The host is : "+nm_scanner['scan'][host]['status']['state']
port_status = "The port 80 is : "+nm_scanner['scan'][host]['tcp'][80]['state']+"/n"
scanning_method = "The scanning method is : "+nm_scanner['scan'][host]['tcp'][80]['reason']+"/n"
#os_fingerprint = "The accuracy is : "+nm_scanner['scan'][host]['osmatch'][0]['accuracy']+" that the host is running "+nm_scanner['scan'][host]['osmatch'][0]['name']+"/n"

with open("host.txt","w+") as f:
    f.write(host_status+port_status+scanning_method)
    f.write("Report Generated : "+time.strftime("%Y-%m-%d_%H:%M:%S GMT",time.gmtime()))
    
print("Finished...")