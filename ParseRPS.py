import requests
import bs4
from bs4 import BeautifulSoup

def viewRPSLink(index, links):
	if (index < 0 or index >= len(links)):
		print('Invalid Number Entered -- Please Try Again')
		return
	else:
		linkUrl = links[index][1]
		linkResponse = requests.get(linkUrl)
		linkSoup = BeautifulSoup(linkResponse.text)
		divs = linkSoup.findAll('div')
		for div in divs:
			if (div.has_attr('class')):
				if (div['class'][0] == 'entry'):
					entryDiv = div
					break;
		entryParagraphs = entryDiv.findAll('p')
		for p in entryParagraphs:
			print(p.text.encode('ascii', 'ignore').decode('ascii', 'ignore'))

def displayFrontPage(headlines):
	print("**************************************")
	print("Rock Paper Shotgun Front Page Stories!")
	print("**************************************")

	linkNumber = 0

	for headline, link in headlines:
		print('[' + str(linkNumber) + ']')
		print(headline)
		print(link)
		print()
		linkNumber += 1

	print("**************************************")

rpsUrl = "http://www.rockpapershotgun.com"

rpsResponse = requests.get(rpsUrl)

rpsSoup = BeautifulSoup(rpsResponse.text)

h2Tags = rpsSoup.findAll('h2')

aTags = []

for h2 in h2Tags:
	aTags.append(h2.find('a'))

headlines = []

for a in aTags:
	try:
		headlines.append((a.contents[0].encode('ascii','ignore').decode('ascii', 'ignore'), a['href']))
	except:
		continue



choice = 0

while (choice != -1):
	displayFrontPage(headlines)
	choice = int(input("Enter a number to view a link\nEnter -1 To Exit: "))
	if (choice != -1):
		viewRPSLink(choice, headlines)
		input("Press Any Key To Display The List Of Links Again")

