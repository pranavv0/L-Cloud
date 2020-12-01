#!/usr/bin/python

# SaaS

import _thread
import os
import subprocess

sip = "192.168.43.65"


def start(a):
	#commands.getstatus(a)
        subprocess.getstatusoutput(a)
	#os.system(a)
        
def call(uname,upass,choice):
	ch = None
	choice = choice.lower()
	if choice == 'gedit':
		ch = 'gedit'
	elif choice == 'browser' :
		ch = 'firefox'
	elif choice == 'vncviewer':
		ch = 'vncviewer'
	
	a= "sshpass -p "+ upass +" ssh -X " + uname +"@"+ sip + "  " + ch
	_thread.start_new_thread(start,(a,))
	print (a)
	
