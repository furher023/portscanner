
import socket as sc
import  termcolor

def scan(target,ports):
	print("\n" + "Scanning target ip :" + target)
	for port in range(1,ports):
		port_scan(target,port) 

def port_scan(ip,port):
	try:
		sock = sc.socket()
		sock.connect((ip,port))
		print("[+] Port open : " + str(port))
		sock.close()
	except:
		pass

targets =input("[*] Enter the targets( seperated by ,):")
ports = int(input("[*] Enter the no. of ports to scan:"))

if "," in targets:
	for target in targets.split(","):
		scan(target.strip(' '),ports)
else:
	scan(targets,ports) 
