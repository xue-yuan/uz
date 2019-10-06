#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

# file
source = os.getcwd() + sys.argv[3]
# directory
target = sys.argv[1]
# coding
encoding = sys.argv[2]

print "Processing File..." \
	+ "\nSource:			" + source \
	+ "\nTarget:			" + target \
	+ "\nEncoding:		" + encoding

file = zipfile.ZipFile(source, "r");

for name in file.namelist():
	decode_name = name.decode(encoding)

	target_path = target + '/'
	if os.path.isabs(target):
		path_name = target_path
	else:
		if target[:2] == '~/':
			path_name = os.getcwd() + '/' + target[2:] + os.path.dirname(decode_name)
		else:
			path_name = os.getcwd() + '/' + target_path
	
	print "extracting: " + decode_name
	
	'''
	print path_name
	'''

	if (not os.path.exists(path_name + decode_name)) and decode_name[-1] == '/':
		os.makedirs(path_name + decode_name)
		print decode_name[-1]
	data = file.read(name)
	
	if os.path.isdir(decode_name):
		continue
	else:
		unzip = open(path_name + decode_name, "w")
		unzip.write(data)
		unzip.close
file.close()
