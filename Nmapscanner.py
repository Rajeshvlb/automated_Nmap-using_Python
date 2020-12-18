#!/bin/bash/python3
import os

if os.access('/root', os.R_OK|os.X_OK):
    os.chdir('/root')
else:
    print("Please run it as root...")

import nmap
scanner = nmap.PortScanner()
print(""".....................................
.....................................
.....................................""")
print("Welcome to Nmap")
print("Using Nmap version: ", scanner.nmap_version())
print(""".....................................
.....................................
.....................................""")
ipaddr = input("Please enter the IP you want to scan: ")
ipaddr = str(ipaddr)
opin = input("""\n Please select the type of scan you want to perform
                1) SYN ACK SCAN
                2) UDP SCAN
                3) COMPREHENSIVE SCAN
                4) FAST SCAN
                5) EXIT\noption: """)
if opin == '5':
    exit
elif opin == '1':
    print("Please wait Nmap is scanning the TCP...\nPress Ctrl+C to terminate.....")
    scanner.scan(ipaddr, '1-1024', '-v -sS')
    #print(scanner.scaninfo())#
    print("IP Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports:", scanner[ipaddr]['tcp'].keys())
    exit
elif opin == '2':
    print("Please wait Nmap is scanning the UDP...\nPress Ctrl+C to terminate.....")
    scanner.scan(ipaddr, '1-1024', '-sU -v')
   # print(scanner.scaninfo())#
    print("IP Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports:", scanner[ipaddr]['udp'].keys())
    exit
elif opin == '3':
    print("Please wait Nmap is handling COMPREHENSIVE scan...\nPress Ctrl+C to terminate.....")
    scanner.scan(ipaddr, '1-1024', '-v -sV -sC -sS -A -O')
    #print(scanner.scaninfo())#
    print("IP Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports:", scanner[ipaddr]['tcp'].keys())
    exit
elif opin == '4':
    print("Please wait Nmap is scanning FASTly...\nPress Ctrl+C to terminate.....")
    scanner.scan(ipaddr, None, '-F')
   # print(scanner.scaninfo())#
    print("IP Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports: ", scanner[ipaddr]['tcp'].keys())
    exit
print("""Thank you for using Nmap.........
                    
        ............THE SCRIPT By....................
                    
        .......................HATEOFFICIAL""")
