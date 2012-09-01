#!/usr/bin/python
# -.- coding: utf-8 -.-

import hashlib
import sys
import os

def md5sum(file_name):
	"""
	return the file's md5sum
	"""
	fd = open(file_name, "rb")
	md5 = hashlib.md5()
	for data in iter(lambda: fd.read(128), ""):
		md5.update(data)
	fd.close()
	return md5.hexdigest()

def md5path(path):
	"""
	return the path md5sum
	if path is a file than return md5sum of the file
	if path is a dir use all the file's/dir's (Lexicographical order) md5sum to do md5sum again
	"""
	if os.path.isfile(path):
		return md5sum(path)
	else:
		md5 = hashlib.md5()
		fileList = os.listdir(path)
		fileList.sort()
		for f in fileList:
			md5.update( md5path( path + '/' + f ) )
	return md5.hexdigest()

if __name__ == '__main__':

	if len(sys.argv) < 1:
		exit(1)
	print md5path( sys.argv[1] ), " " + sys.argv[1]
