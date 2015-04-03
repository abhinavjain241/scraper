# Abhinav Jain : Summer Internship Task for SocialCops 
# Individual Spider - Crawls through the individual links and finds links to PDF's
import os
import scrapy

#Open file 'urls' for reading in links to different press releases
f = open('urls', 'r')
#Open file 'final' for writing final links to PDF's
g = open('final','w')

class TraiSpider(scrapy.Spider):
	name = "indi"
	allowed_domains = ["http://trai.gov.in/"]
	start_urls = []
	for line in f:
		line = line.split("\n")[0]
		start_urls.append(line)

	def parse(self, response):
		for sel in response.xpath('//a/@href').extract():
			if(len(sel.split(".")) > 1):
				if(sel.split(".")[1]=='pdf'):
					g.write("http://trai.gov.in" + sel + "\n")

