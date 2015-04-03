# Abhinav Jain : Summer Internship Task for SocialCops 
# TRAI Spider - Crawls through the given page containing links to the different press releases 
import scrapy

f = open('urls','w')

class TraiSpider(scrapy.Spider):
	name = "trai"
	allowed_domains = ["http://trai.gov.in/"]
	start_urls = [
		"http://trai.gov.in/Content/PressReleases.aspx"
	]

	def parse(self, response):
		for sel in response.xpath('//a/@href').extract():
		    if(len(sel.split("/")) > 2):
		        if(sel.split("/")[2] == 'PressDetails'):
		            f.write("http://trai.gov.in" + sel + "\n")
