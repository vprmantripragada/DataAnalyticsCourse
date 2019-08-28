#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
#import pymongo


def init_browser():
    # URL of page to be scraped
    #pointing to the directory where chromedriver exists
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()

# # Scrape : Nasa News Site 
    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html,'html.parser')

    news_title = soup.find('div',class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    print(f"News Title: {news_title}")
    print(f"News Paragraph: {news_p}")



# # Scrape : Nasa Featured image
    url_images = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_images)

    html = browser.html
    soup = bs(html,'html.parser')

    image = soup.find('article', class_='carousel_item')
    image.footer

    image_url= image.footer.a['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url
    #print(featured_image_url)



# # Scrape : Mars Weather
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weather)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html,'html.parser')

    mars_weather_gp= soup.find('div', class_='tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet has-cards has-content')
    mars_weather = mars_weather_gp.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text

    #print(mars_weather)


# # Scrape : Mars Facts
    url_facts = 'https://space-facts.com/mars/'

    tables = pd.read_html(url_facts)
    tables

    df = tables[1]

    df.columns = ['Parameters', 'Values']
    #df1 =df.set_index('Parameters')
    df

    html_table = df.to_html()
    #html_table.replace('\n', '')
    df.to_html('table.html')


    # #  Scrape : Mars Hemisphere
    url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemi)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html,'html.parser')

    # determine urls to individual images
    hemi_url = []
    results_hemi = soup.find_all('div', class_='item')

    for result in results_hemi:
        url = result.a['href']
        hemi_url.append(url)
#hemi1
    hemi1 ={}

    url1 = 'https://astrogeology.usgs.gov' + hemi_url[0]
    #print(url1)

    browser.visit(url1)
    html1 = browser.html
        
    soup = bs(html1,'html.parser')
    image = soup.find('div', class_='downloads')

    hemi1["url1"] = image.ul.li.a['href']

    hemi1['title1'] = soup.find('h2', class_='title').text
    #print(hemi1)
    hemi1_url = hemi1['url1']
    hemi1_title = hemi1['title1']
#hemi2
    hemi2 ={}

    url2 = 'https://astrogeology.usgs.gov' + hemi_url[1]
    #print(url2)

    browser.visit(url2)
    html2 = browser.html
        
    soup = bs(html2,'html.parser')
    image = soup.find('div', class_='downloads')

    hemi2["url2"] = image.ul.li.a['href']

    hemi2['title2'] = soup.find('h2', class_='title').text
    #print(hemi2)
    hemi2_url = hemi2['url2']
    hemi2_title = hemi2['title2']
#hemi3
    hemi3 ={}

    url3 = 'https://astrogeology.usgs.gov' + hemi_url[2]
    #print(url3)

    browser.visit(url3)
    html3 = browser.html
        
    soup = bs(html3,'html.parser')
    image = soup.find('div', class_='downloads')

    hemi3["url3"] = image.ul.li.a['href']

    hemi3['title3'] = soup.find('h2', class_='title').text
    hemi3_url = hemi3['url3']
    hemi3_title = hemi3['title3']

    hemi4 ={}

    url4 = 'https://astrogeology.usgs.gov' + hemi_url[3]
    #print(url4)

    browser.visit(url4)
    html4 = browser.html
        
    soup = bs(html4,'html.parser')
    image = soup.find('div', class_='downloads')

    hemi4["url4"] = image.ul.li.a['href']

    hemi4['title4'] = soup.find('h2', class_='title').text
    hemi4_url = hemi4['url4']
    hemi4_title = hemi4['title4']

    mars_info = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "html_table": html_table,
        "hemi1_url": hemi1_url,
        "hemi2_url": hemi2_url,
        "hemi3_url": hemi3_url,
        "hemi4_url": hemi4_url,
        "hemi1_title": hemi1_title,
        "hemi2_title": hemi2_title,
        "hemi3_title": hemi3_title,
        "hemi4_title": hemi4_title
     } 

    # Close the browser after scraping
    browser.quit()

        # Return results
    return mars_info
