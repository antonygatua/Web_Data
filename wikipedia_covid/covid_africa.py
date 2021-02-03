import pandas as pd
import numpy as np

import time 

import requests 
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrapycovid():
    url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Africa'

    html = urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')
    
    covid_table = soup.find('table', class_="wikitable sortable plainrowheaders")
    
    # number of rows in the table including header
    rows = covid_table.findAll("tr")
    len(rows)
    
    # header attributes of the table
    header = [th.text.rstrip() for th in rows[0].find_all('th')]
    
    # create a dictionary
    covid = dict([(x,0) for x in header])
    
    data = list(covid_table.find_all('tr'))
    data.pop(0)
    data.pop() 
    
    countries = []
    confirmed_cases = []
    active_confirmed_cases = []
    recoveries = []
    deaths = []
    ref = []
    for country in data:
        countries.append(country.find('a').get_text().strip())
    for row in data:
        values = row.findAll('td')
        if len(values) == 5:
            confirmed_cases.append(values[0].find(text=True).strip())
            active_confirmed_cases.append(values[1].find(text=True).strip())
            recoveries.append(values[2].find(text=True).strip())
            deaths.append(values[3].find(text=True).strip())
            ref.append(values[4].find('a', href=True, text = True))
    covid['Country'] = countries
    covid['Confirmed cases'] = confirmed_cases
    covid['Active confirmed cases'] = active_confirmed_cases
    covid['Recoveries'] = recoveries
    covid['Deaths'] = deaths
    covid['Ref.'] = ref
    
    data = pd.DataFrame(covid)
        
    data.to_csv('covid_data.csv')
    
    return data.head()


scrapycovid()