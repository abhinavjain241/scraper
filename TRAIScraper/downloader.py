# Abhinav Jain : Summer Internship Task for SocialCops 
# Downloader Script - To download all the PDF's from the list of the links																				
import os
import urllib

if not os.path.exists("files"):
	os.makedirs("files")

f = open('final','r')

for line in f:
	testfile = urllib.URLopener()
	fname = line.split("/")[-1]
	print "Downloading file " + fname
	testfile.retrieve(line,"files/" + fname)

print "All files have been downloaded and are placed in the 'files' directory!"