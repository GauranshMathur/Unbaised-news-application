from pynytimes import NYTAPI
import pandas as pd
import json
import os
import csv

secretAPIkey = 'Gm8eOJ2OJNb2qj60ZUqgAs1yavEof2Y6'
nyt = NYTAPI(secretAPIkey, parse_dates=True)

most_viewed = nyt.article_search(
    query = "goverment",
    results = 100
)


f = open('data.csv', 'w')
writer = csv.writer(f)
writer.writerow(['title'])



for i in range(0, len(most_viewed)):
    writer.writerow([str(most_viewed[i]['headline']['main'])])

f.close()