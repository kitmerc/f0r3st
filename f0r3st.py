#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import socket
import os
import sys
import time

#icon
warning_banner =  "error: "
clean_space = " " * 20
sec_space = " " * 15
def icon(status):
    if (status == 1):
        print()
        print()
        print(clean_space ,"░                     \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒                    \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓                   \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█                  \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█                  \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0              \r", end ="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r            \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3          \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s        \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t      \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t █    \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t █▒   \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t █▒▓  \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ F 0 r 3 s t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f x r 3 s t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 R 3 s t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r $ s t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 S t █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s T █▒▓░ \r", end="")
        time.sleep(0.125)
        print(clean_space ,"░▒▓█ f 0 r 3 s t █▒▓░ \r", end="")
        print()
        print()
    else:
        print()
        print(sec_space ,"i wish you good finds! goodbye   \r", end="")
        time.sleep(0.3)
        print(sec_space ,"i wish you good finds! goodbye.  \r", end="")
        time.sleep(0.3)
        print(sec_space ,"i wish you good finds! goodbye.. \r", end="")
        time.sleep(0.3)
        print(sec_space ,"i wish you good finds! goodbye...\r")
        time.sleep(0.3)

#arguments
ports = []
if("-help" in sys.argv):
    print()
    print("Use: python3 f0r3st.py -host [ip/domain]")
    print("Additional flags:")
    print("-port [80|80-443]— specify port range for scan, by default 1-10000")
    print("-v - more interesting information, for example OS")
    print()
    exit()
if("-host" in sys.argv):
    start_index=sys.argv.index("-host")
    try:
        host=sys.argv[start_index+1]
    except IndexError:
        print("Something wrong, see -help")
        exit()
if("-port" in sys.argv):
    start_index_second=sys.argv.index("-port")
    try:
        ports=sys.argv[start_index_second+1]
        if("-" in ports):
            ports=ports.split("-")
            ports=[int(ports[0]),int(ports[1])]
            for i in range(ports[0],ports[1]):
                ports.append(i)
        else:
            ports=[int(sys.argv[start_index_second+1])]
    except IndexError:
        print("Something wrong, see -help")
        exit()   
else:
    for i in range(1,10000):
        ports.append(i)      
icon(1)

#check host
check_host = os.system("ping -c 1 " + host + " >> /dev/null")
if (check_host==0):
    print("Nice! Host is active!")
if (check_host!=0):
    print("Ooops! Host is not responsed!")
    wait=input("Do you want to continue? Y/N: ")
    if(wait=="Y" or wait=="y"):
        pass
    else:
        print("Sorry... Not today...")
        exit()
print("Go to scan!")
start_time=time.time()

#function scan
list_openned = []
def scanner(port):
    sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect_sock  = sock.connect((host, port))
        list_openned.append(port)
        connect_sock.close()
    except:
        pass
    
#threading
for i in ports:
    try:
        thread = threading.Thread(target=scanner, kwargs={'port': i})
        thread.start()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        pass
threads_list=int(threading.active_count())
while threads_list>1:
    threads_list=int(threading.active_count())
    time.sleep(0.000001)

#list ports
print("*" * 30)
for port in list_openned:
    if (port == 20):
            print(  port , "port open" ,  "it's FTP-DATA")
    elif port == 21:
            print(  port , "port open" ,  "it's FTP")
    elif port == 22:
            print(  port , "port open" ,  "it's SSH")
    elif port == 23:
            print(  port , "port open" ,  "it's Telnet")
    elif port == 25:
            print(  port , "port open" ,  "it's SMTP")
    elif port == 43:
            print(  port , "port open" ,  "it's WHOIS")
    elif port == 53:
            print(  port , "port open" ,  "it's DNS")
    elif port == 80:
            print(  port , "port open" ,  "it's http")
    elif port == 115:
            print(  port , "port open" ,  "it's SFTP")
    elif port == 123:
            print(  port , "port open" ,  "it's NTP")
    elif port == 143:
            print(  port , "port open" ,  "it's IMAP")
    elif port == 161:
            print(  port , "port open" ,  "it's SNMP")
    elif port == 179:
            print(  port , "port open" ,  "it's BGP")
    elif port == 443:
            print(  port , "port open" ,  "it's HTTPS")
    elif port == 445:
            print(  port , "port open" ,  "it's MICROSOFT-DS")
    elif port == 514:
            print(  port , "port open" ,  "it's SYSLOG")
    elif port == 515:
            print(  port , "port open" ,  "it's PRINTER")
    elif port == 993:
            print(  port , "port open" ,  "it's IMAPS")
    elif port == 995:
            print(  port , "port open" ,  "it's POP3S")
    elif port == 1080:
            print(  port , "port open" ,  "it's SOCKS")
    elif port == 1194:
            print(  port , "port open" ,  "it's OpenVPN")
    elif port == 1433:
            print(  port , "port open" ,  "it's SQL Server")
    elif port == 1723:
            print(  port , "port open" ,  "it's PPTP")
    elif port == 3128:
            print(  port , "port open" ,  "it's HTTP")
    elif port == 3268:
            print(  port , "port open" ,  "it's LDAP")
    elif port == 3306:
            print(  port , "port open" ,  "it's MySQL")
    elif port == 3389:
            print(  port , "port open" ,  "it's RDP")
    elif port == 5432:
            print(  port , "port open" ,  "it's PostgreSQL")
    elif port == 5060:
            print(  port , "port open" ,  "it's SIP")
    elif port == 5900:
            print(  port , "port open" ,  "it's VNC")
    elif port == 8080:
            print(  port , "port open" ,  "it's Tomcat")
    elif port == 10000:
            print(  port , "port open" ,  "it's Webmin")
    else:
            print(  port , "port open" ,  "it's unknown")

print("*" * 30)
print("Total time: " + str(round(time.time()-start_time)) + "sec")

#vuln
if ("-v" in sys.argv):
    check_os = os.system('''nmap -O ''' + host + '''| grep 'OS details' | cut -c 13- > detectOS ''')
    with open('./detectOS','r',encoding = 'utf-8') as f:
        check_os = f.readline()
        check_os = ''.join([line.rstrip('\n') for line in check_os])
        f.close()
    if (check_os == ''):
        check_os = 'Hmm... OS not defined '
    print()
    print(clean_space, 'Interesting artifacts:', '\n')
    print('OS on this host: ', check_os)
icon(0)
print()
