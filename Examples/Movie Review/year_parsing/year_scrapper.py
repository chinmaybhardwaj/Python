from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from selenium import webdriver

# =============================================================================
# Parse HTML and get links for each year.
# URL: https://en.wikipedia.org/wiki/Lists_of_films
# =============================================================================


base_url = 'https://en.wikipedia.org'

#
# Request HTML page for url
#
def get_year_page(url=''):
    response = requests.get(url)
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response = session.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
#    
#    browser = webdriver.Firefox()
#    browser.get(url)
#    
#    html = browser.page_source
#    soup = BeautifulSoup(html, features="html.parser")
    return soup

#
# Save HTML response to Lists_of_films.html file in source directory
#
def save_html(name, soup):
    outputdir = './source/html'
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
        
    # Write HTML String to .html file
    filename = outputdir + '/' + name + '.html'
    with open(filename, "w") as file:
        file.write(str(soup.encode("utf-8")))
        print(name,'html created!')  
    
    
#
# Load HTML response from Lists_of_films.html
#
def load_html(name):
    outputdir = './source/html/' + name + '.html'
    if not os.path.exists(outputdir):
        print(name, 'html does not exist!')
        return None
        
    # Read HTML String from Lists_of_films.html
    with open(outputdir, "r") as file:
        soup = BeautifulSoup(file, features="html.parser")
        print('Loading', name, 'html !')  
        
    return soup


#
# Parse HTMl to get list of all years and their links
#
def parse_html(divs):
    href = []
    text = []
    for mydiv in divs:
        dt_a = mydiv.find_all("a", href=True)
        print(mydiv)
        for a in dt_a:
            print(a.text, '-------', a["href"])
            href.append(a["href"])
            text.append(a.text)
        
    return text, href


#
# Save Years and Links to years_table.csv
#
def save_to_csv(name, text=[], href=[]):
    outputdir = './source/csv/'
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
        
    # Write DataFrame to years.csv
    df = pd.DataFrame()
    df['year'] = text
    df['link'] = href
    csv_name = outputdir + name + '.csv'
    df.to_csv(csv_name, sep=',', index=False, encoding='utf-8')
    print(name, 'csv created!')  
    
    
    
#
# Load dataframe from year.csv
#    
def load_years_csv(name):
    outputdir = './source/csv/' + name + '.csv'
    if not os.path.exists(outputdir):
        print(name, 'csv does not exist!')
        return None
        
    # Read DataFrame from year.csv
    with open(outputdir, "r") as file:
        df = pd.read_csv(file)
        print('Loading', name, 'csv !') 
        
    return df
    

#
# Main function to check if csv/html file exists or not.
# If file does not exist request html page and parse response
#
def get_year(name='', url=''):

    df = load_years_csv(name)
    
    if df is None:
        soup = load_html(name)
        if soup is None:
            soup = get_year_page(url = base_url + url) 
            save_html(name, soup)
        
        mydivs = soup.findAll("table",{"class":"wikitable sortable jquery-tablesorter"})
        text, href = parse_html(mydivs)
        save_to_csv(name, text=text, href=href)
        
    else:
        print('CSV ready to use!')
        return df

        
