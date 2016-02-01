#!/usr/bin/python
import urllib2,HTMLParser,re
import datetime
import os
host = "http://disa.csie.ntu.edu.tw/~janetyc/data"
directory = "/tmp2/yuchen/R324_20141022/"
def downloadImage(url):
	cont = urllib2.urlopen(url).read()
	pattern = 'image_[0-9-]*\.jpg';
	match = re.search(pattern, url);
	if match:
		print 'downloading',match.group()
                filename = directory+match.group()
		dir = os.path.dirname(filename)
		try:
			os.stat(dir)
		except:
			os.mkdir(dir) 
		f = open(filename,'wb')
		f.write(cont)
		f.close()
	else:
		print 'no match'

start_date = datetime.datetime(2014, 10, 22)
#image

for single_date in (start_date + datetime.timedelta(n) for n in range(1)):
	date_str = single_date.strftime('%Y%m%d')
	print date_str
	for single_time in (single_date + datetime.timedelta(0,300*n) for n in range(24*60/5)):
		downloadImage(host+'/'+date_str+'/image_'+date_str+'-'+single_time.strftime('%H%M')+'.jpg')

