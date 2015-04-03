if [ ! -w "urls" ]; then 
	touch urls
fi 
scrapy crawl trai
scrapy crawl indi
python downloader.py