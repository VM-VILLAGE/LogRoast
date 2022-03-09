import re 
import json	
import urllib.request
import platform
import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def oslogging():
	if platform.system() == "Windows":
		filelocation = "C:\\Windows\\System32\\logfiles\\firewall\\pfirewall.log"
		if not os.path.exists(filelocation):
			subprocess.call('powershell.exe -command set-netfirewallprofile -name Private -logallowed True', shell=True)
			messagebox.showinfo('Log files not found', 'We have enabled logging on your firewall. Please return back when the log file becomes populated')
	return filelocation

def getlogs():
	for line in lines:
		if re.findall(r'\d+\.\d+\.\d+\.\d+.*SEND$', line) != []:
			greg = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
			line = greg[1]
			ip_list.append(line)
		else:
			continue

def listing():
	for ip in ip_list:
		freq_list.append(ip_list.count(ip))
	index = 0
	for num in freq_list:
		ip_list.insert(index, str(num))
		index += 2

def list_to_string():
	index = 0
	while index < len(ip_list):
		tony = " ".join(ip_list[index:(index + 2)])
		col_list.append(tony)
		index += 2

def ipfind(data):
	ip = data
	response = urllib.request.urlopen("http://ipwhois.app/json/" + ip)
	ipgeolocation = json.load(response)
	return ipgeolocation.get('org')

def final():
	output = set(col_list)
	for line in output:
    		line = line.split(' ') 
    		fin_list.append(line[0])
    		fin_list.append(line[1])
	index = 2
	for line in fin_list[1::2]:
			tony = ipfind(line)
			fin_list.insert(index, str(tony))
			index += 3

def GUI():
	table = Tk()
	table.title('LogRoast')
	table.geometry('1000x1000')
	table['bg'] = 'white'

	table_frame = Frame(table)
	table_frame.pack()

	my_table = ttk.Treeview(table_frame, height=500)

	my_table['columns'] = ('OCCURANCES', 'IPADDRESS', 'COMPANY')

	my_table.column("#0", width=0, stretch=NO)
	my_table.column("OCCURANCES", anchor=CENTER, width=250)
	my_table.column("IPADDRESS", anchor=CENTER, width=250)
	my_table.column("COMPANY", anchor=CENTER, width=250)
	my_table.heading("#0", text="", anchor=CENTER)
	my_table.heading("OCCURANCES", text="OCCURANCES SINCE " + str(date), anchor=CENTER)
	my_table.heading("IPADDRESS", text="IPADDRESS", anchor=CENTER)
	my_table.heading("COMPANY", text="COMPANY", anchor=CENTER)

	my_table.pack()

	index = 0
	number = 0
	while number < len(fin_list) // 3:
   		my_table.insert(parent='', index='end', text='', values=(fin_list[index], fin_list[index + 1], fin_list[index + 2]))
   		index += 3
  	 	number += 1

	table.mainloop()

ip_list = []
freq_list = []
col_list = []
fin_list = []

file = open(oslogging(), 'r')
lines = file.read().splitlines()
startdate = re.findall(r'\d+\-\d+\-\d+', lines[6])
date = startdate.pop(0)

getlogs()
listing()
list_to_string()
final()
GUI()

