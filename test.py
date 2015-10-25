from bs4 import BeautifulSoup
import urllib
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
	links= soup.find_all('p')
	#description= soup.find_all('p', 'web-result-description')
	for i in range(3):
		print links[i].contents

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
		choiceCheck(raw_input("Please enter 1 or 2: "))






for i in range(3):
	print "Search Round ", i+1, '\n'
	query=raw_input("Enter a search: ")
	print "Start Searching ----------------------------------------------------------------------------------------"
	googleSearch(query)
	print "Searching ----------------------------------------------------------------------------------------------"
	askSearch(query)
	print '\n\n'
	choiceCheck(raw_input("choose 1 or 2: "))

print "Result: ", googleCount, " vs " , askCount

