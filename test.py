from bs4 import BeautifulSoup, SoupStrainer
import urllib
import httplib2
import json


def stripper(text):
    return text.lower().replace('\n',''
                      ).replace('\f',''
                      ).replace('\v',''                      
                      ).replace('\t',''
                      ).replace('\r',''
                      ).replace(' ',''
                      ).replace('</br>',''
                      ).replace('<br/>',''
                      ).replace('<br>',''
                      ).replace(',',''
                      ).replace('.',''
                      ).replace('<p>',''
                      ).replace('</p>',''
                      )

def googleSearch(query):
	encoded = urllib.quote(query) 
	rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()
	jsonData = json.loads(rawData)




	searchResults = jsonData['responseData']['results']
	for result in searchResults:
		title= result['title']
		link = result['url']
		print stripper(title)
		print link
		print '\n'


def askSearch(query):
	encoded = urllib.quote(query)
	rawData = urllib.urlopen('http://www.ask.com/web?q=' + encoded).read()
	soup = BeautifulSoup(rawData)
	all_links= soup.find_all('p', class_="web-result-url")
	all_links_desc = soup.find_all('p', class_="web-result-description") 

	for i in range(3):
		print unicode(all_links[i].contents[0])
		print unicode(all_links_desc[i])
		print '\n'

googleCount = 0
askCount = 0


def choiceCheck(choice):
	global googleCount
	global askCount
	if int(choice) == 1:
		googleCount = googleCount + 1

	elif int(choice) == 2:
		askCount = askCount + 1

	else:
		choiceCheck(raw_input("Please select the better result 1 or 2: "))






for i in range(3):
	print "Search Round ", i+1, '\n'
	query=raw_input("Enter a search: ")
	print "Start Searching using engine-1 ----------------------------------------------------------------------------------------"
	googleSearch(query)
	print "Now searching using engine-2 ----------------------------------------------------------------------------------------------"
	askSearch(query)
	print '\n\n'
	choiceCheck(raw_input("Please select the better result  1 or 2: "))

print "Result: ", googleCount, " vs " , askCount

