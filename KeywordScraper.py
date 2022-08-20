import requests
from bs4 import BeautifulSoup
import csv

def add_plus(keywords):
	keywords = keywords.split()
	keyword_edited = ""
	for i in keywords:
		keyword_edited += i + "+"
	keyword_edited = keyword_edited[:-1]
	return keyword_edited
	
class KeywordScraper:
        def __init__(self, keyword):
                self.keyword = keyword
                plusified_keyword = add_plus(keyword)
                self.keywords_scraped = []
                self.search_string = "https://www.google.com/search?q=" + plusified_keyword + "&tbm=nws"
		
        def scrape(self):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
                content = requests.get(self.search_string, headers=headers).text
                soup = BeautifulSoup(content, "html.parser")
                #print(soup)
                
                related_keyword_section = soup.find_all("div", {"class":"GI74Re nDgy9d"})
                
                for i in range(0,len(related_keyword_section)-1):
                    self.keywords_scraped.append(related_keyword_section[i].get_text().lstrip().rstrip())
                
               
        def write_to_file(self):
            with open("scraped keywords.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow(self.keywords_scraped)
                print("keywords related to " + self.keyword + " scraped successfully")
                        

