#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Akos Daniel daniel.akos77ATgmail.com
#
# Filename: sensorupdater.py
# Current Version: 0.1 beta
# Created: 20 of Jun 2017
# Last Changed: 20 of Jun 2017
# -----------------------------------------------------------------------------------------------
# Description:
# -----------------------------------------------------------------------------------------------
# This script logs in the prtg server and change the channel settings according to the values in ini file, that must be a json file, see example file!
# Step 1.
# For the login you need a hashkey. Open the following page on the firewall with a credential, example:
# http://yourprtgserverip/api/getpasshash.htm?username=yourusername&password=yourpassword
# In the output is your hashkey.
# Step 2.
# After that just test it like this example (change the IP and the key for you!):
# $ ./sensorupdater.py -host 1.1.1.1 -user root -pass 123 -ini ini.json
# Done...
#
# Syntax:
# -------
# $ ./sensorupdater.py -host <prtg-srv-ip> -user <username> -pass <password> -ini <inifile>
#
# Mandatory arguments:
# --------------------
# <prtg-srv-ip>			: The IP or hostname of the prtg server.
# <username>			: Username for the logon on prtg.
# <password>			: The password
# <inifile>				: The ini file in json format

# Output:
# -------
# prints the following output:
# Done...
#
# Example:
# --------
# $ ./sensorupdater.py -host 1.1.1.1 -user prtgadmin -pwd admin1234 -file ini.json
# Done...
# -----------------------------------------------------------------------------------------------
# Known issues:
# 
# -----------------------------------------------------------------------------------------------
# [solved]
# -----------------------------------------------------------------------------------------------
# Change History
#
# -----------------------------------------------------------------------------------------------
# 0.1 beta: (20 of Jun 2017)

import sys, getopt
import json
import xml.etree.ElementTree as ET
import urllib2
from urllib2 import quote
import pdb
import argparse
import logging

def main(argv):
	
	#0. check the arguments
	
	parser = argparse.ArgumentParser(description='PRTG Sensor Bulk Updater.',epilog="And that's how you save your time...")
	parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
	parser.add_argument('host', help='IP or hostname of the prtg server')
	parser.add_argument('user', help='Username for the logon on prtg server.')
	parser.add_argument('pwd', help='Password for the logon on prtg server.')
	parser.add_argument('file', help='The ini file in json format for the filter and new values.')
	
	args = parser.parse_args()
	
	# logging
	
	logging.basicConfig(level=logging.INFO, 
						filename='prtg.log', # log to this file
						format='%(asctime)s %(message)s') # include timestamp
	logging.info("Start Logging...")

	#1. get the hash instead of using the password
	try:
		response = urllib2.urlopen('http://' + args.host + '/api/getpasshash.htm?username=' + args.user + '&password=' + args.pwd )
	except urllib2.HTTPError, error:
		print error.code
		sys.exit()
	
	pwdhash = response.read()
	
	#2. get the sensorlist in xml
	try:
		response = urllib2.urlopen('http://' + args.host + '/api/table.xml?content=sensors&output=xml&columns=objid,group,device,sensor&count=10000&username=' + args.user + '&passhash=' + pwdhash)
	except urllib2.HTTPError, error:
		print error.code
		sys.exit()
	
	xmltable = response.read()
	root = ET.fromstring(xmltable)
	
	#3. open the json ini file
	with open(args.file) as jsdata:
		data = json.load(jsdata)
		
	#4. search for the items and change the tag values
	for entry in root.findall("./item"):
		match = 0
		matchcount = len(data['item'])
		for key, value in data["item"].iteritems():
			filterval = entry.find(key).text
			if isinstance(value,list):
				for i in value:
					#pdb.set_trace()
					if i.startswith('%') and i.endswith('%'):
						i = i[1:-1]
						if str(i) in filterval:
							match += 1
					else:
						if filterval == str(i):
							match += 1
			else:
				if value.startswith('%') and value.endswith('%'):
					value = value[1:-1]
					if str(value) in filterval:
						match += 1
				else:
					if filterval == str(value):
						match += 1
						
		if match == matchcount:
			sensorid = entry.find('objid').text
			print (sensorid)
			for key, value in data["tag"].iteritems():
				if value:
					val = quote(value.encode('utf-8'))
					url = 'http://' + args.host + '/api/setobjectproperty.htm?id=' + sensorid  + '&subid=0&subtype=channel&name=' + key + '&value=' + val + '&username=' + args.user + '&passhash=' + pwdhash
					logging.info(url)
					try:
						urllib2.urlopen(url)
					except urllib2.HTTPError, error:
						print error.code
						logging.info(error.code)

	print "Done..."
	logging.info("End Logging...")
				
if __name__ == "__main__":
	main(sys.argv[1:])