import socket
import sys
import subprocess

subprocess.call('clear', shell=True)

remoteServer=input("enter the host to scan")
remoteServerIP=socket.gethostbyname(remoteServer)

print("_"*60)
print("please wait, scanning undergoing.....",remoteServerIP)
print("_"*60)
try:
     for port in range(1,1025):
         sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         result=sock.connect_ex((remoteServerIP,port))
         if result == 0:
             port("port {}:".format(port))
             sock.close()
except socket.error:
     print("error in reaching host")
     sys.exit()
         
