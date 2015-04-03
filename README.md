## TRAI Scraper

This is the code for the scraper used to crawl the website of Telecom Regulatory Authority of India, as mentioned in the data parser [tasklist](https://drive.google.com/folderview?id=0Bw5Gsp1nAXwbfnhQV2ZXRm9jcm40RUdZR1FhV29rX0kxTGZWY0g4WjRNd3RfTW5hbmhEUUU&usp=drive_web&tid=0Bw5Gsp1nAXwbflNOT0V3QVJ0cjd6WVJySlc4bUw4Zm1LaHdkenpnNE8xS2xwV3dPTkItc1k) for [SocialCops](www.socialcops.org/).  


**Title : ** Data Parsing using Scrapy

**Project Description: ** This project aims at downloading files from hidden links in a given website. For this task, particularly, this [website](http://trai.gov.in/Content/PressReleases.aspx).

**Use Cases and Edge Conditions: ** Currently this program only works for the above mentioned website since it has been written in a particular way the website has been designed. This might be extended to a generic program which extracts links on any given webpage and downloads files they point to.

**Workflow :** This program has been built using the Scrapy library in Python. It involves two spiders(web crawlers), one for the given webpage, and the other one for the extracted links on the first page. The first one parses the given link and returns the URL's of the different webpages of every individual Press Release, which are then sent to the second spider which extracts links to PDF's from the individual webpages, and stores them in another file. Now a third script runs, which processes each link and downloads the corresponding PDF's into a directory called **'files'**.

**Data Formats and Reporting:** As such, there is no particular data format, just PDF files which are the press releases of TRAI. Apart from this, there were two buffer files used for manipulating the list of the links extracted.

**Performance and Scaling : **
This particular application was built keeping only a single website in mind, extracting data from which wasn't very computationally intensive. However, in the future, if this application has to be scaled and used as a massive web crawler.

Scrapy has a Crawler component that includes request scheduler as well as visited urls queue, together with all the configuration parameters related to how the crawling process should be performed. Thus if you want to crawl multiple domains simultaneously the best isolation level would be to create a separate Crawler for each domain. This will allow you to have a custom configuration context per domain.

** Unresolved Issues :** For any unresolved issues, please check issues for this repository.
