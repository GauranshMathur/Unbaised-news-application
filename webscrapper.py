
import pandas as pd
from autoscraper import AutoScraper
import csv

url = 'https://www.bbc.com/'


wanted_list = ["<a href>"] 

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)


    
    

