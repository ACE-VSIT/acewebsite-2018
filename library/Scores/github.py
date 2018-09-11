from lxml import html
import requests

def fetchGithub(username):
	
	url = 'https://github.com/ACE-VSIT/Library-Portal/graphs/contributors'
	page = requests.get(url)

	tree = html.fromstring(page.content)

	contributors = tree.xpath(
		'//div[@id="contributors"]/ol/li/h3/a/text()'
		)
	if username in contributors:
		commits =  tree.xpath(
			'//div[@id="contributors"]/ol/li/h3/span/span/span/text()'
			)
		conIndex = contributors.index(username)
		
		points = commits[conIndex*2:conIndex*2+2]

		return points[0],points[1]
	




#  name = '//div[contains(@class, "fbFeedTickerStory")]/a/div/div/div/div/span/text()'