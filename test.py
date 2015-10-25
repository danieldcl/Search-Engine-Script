import urllib2
from bs4 import BeautifulSoup


webpage = urllib2.urlopen('http://www.ask.com/web?q=pineapple&qsrc=0&o=0&l=dir&qo=homepageSearchBox')
webpage = urllib2.urlopen('https://www.google.com/?gws_rd=ssl#q=pineapple')


soup= BeautifulSoup(webpage.read())
links= soup.find_all('p')
#description= soup.find_all('p', 'web-result-description')

for i in range(6):
	print links[i] ,'\n'
	#print description[i].string , '\n'
