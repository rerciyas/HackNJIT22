from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

from selenium.webdriver.common.by import By

def returnUserAgent():
    AGENTS = []
    agentfile = open("Chromeagents.txt", 'r')
    for line in agentfile.readlines():
        AGENTS.append(line.strip("\n"))
    return random.choice(AGENTS)

def get_url(product_name):
    template = 'https://www.amazon.com/s?k={}&s=review-rank'
    product_name = product_name.replace(' ', '+')
    return template.format(product_name)

def web_scraper():
    opts = webdriver.ChromeOptions()
    opts.add_argument("English(US)=en-US,en;q=0.5")
    opts.add_argument("user-agent=" + returnUserAgent())
    opts.add_argument('window-size=1920x1080')
    opts.add_argument('headless')

    driver = webdriver.Chrome(options=opts)

    products = {}

    ad = False
    i = 0
    j = 0
    lowest = 5000000
    lowestind = 0
    prodlist = []
    lowestlist = []



    prodlist = ['Camping Tent', 'Backpack', 'Sleeping bag', 'Flashlight', 'Sleeping pad',
                'Pillow', 'First Aid Kit']
    for search in prodlist:
        url = get_url(search)

        driver.get(url)
        time.sleep(2)
        html_doc = driver.page_source

        soup = BeautifulSoup(html_doc, 'html.parser')

        for script in soup.find_all('script', src=False):
            script.decompose()

        #print(soup.prettify())

        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        while j < 21 and i < len(results): #change how many compared in the list
            item = results[i]
            atag = item.h2.a
            description = atag.text.strip()

            #get review count
            rev_count = item.find('span', {'class': 'a-size-base puis-light-weight-text s-link-centralized-style'})
            if rev_count != None:
                rev_count = item.find('span', {'class': 'a-size-base puis-light-weight-text s-link-centralized-style'}).text
                rev_count = rev_count.replace(',', '')
            else:
                rev_count = item.find('span', {'class': 'a-size-base s-underline-text'})
                if rev_count != None:
                    rev_count = item.find('span', {'class': 'a-size-base s-underline-text'}).text
                    rev_count = rev_count.replace(',', '')
                else:
                    ad = True
            
            if ad is False:
                if int(rev_count) > 50:
                    #get the price
                    try:
                        url = 'https://www.amazon.com' + atag.get('href')
                        price_parent = item.find('span', 'a-price')
                        price = price_parent.find('span', 'a-offscreen').text
                        price = price.replace('$','')
                        price = price.replace(',','')
                    except AttributeError:
                        price = '100000'

                    #find lowest price
                    if (float(price) < lowest):
                        lowest = float(price)
                        lowestind = j
                        

                    #get the ratings
                    rating = item.i.text

                    #add the review count

                    info = (description, price, rating, rev_count, url)
                    products[j] = info;
                    j += 1
            i += 1
            if ad is True:
                j += 1
            ad = False
        lowestlist.append(products[lowestind])
        j = 0
        i = 0
        
    return(lowestlist)