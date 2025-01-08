import requests
from bs4 import BeautifulSoup

def webscraper():
    #scraping the daily devotions from Proverbs 31 Ministries
    dailydevotionsURL = "https://proverbs31.org/read/devotions";
    page = requests.get(dailydevotionsURL);
    soup = BeautifulSoup(page.content, 'html.parser');
    devotionsBody = soup.find('div', class_='col-sm-8 teaser-body');
    indivURL = devotionsBody.find('a')['href'];
    indivURL = "https://proverbs31.org/read/" + indivURL

    #format for each devotion
    page = requests.get(indivURL);
    soup = BeautifulSoup(page.content, 'html.parser');

    title = soup.find('h1', attrs={'data-sf-field': 'Title'}).get_text(strip=True);
    verse = soup.find('blockquote').get_text();
    blogBody = soup.find('div', id='blogBody');
    img = blogBody.find('img')['data-src'];
    marker = blogBody.find('h4');
    conclusion = marker.find_previous_sibling('p').findPrevious().get_text();

    scrapped_data = {
        "Title:": title,
        "Verse:": verse,
        "Image": img,
        "Read": conclusion,
        "URL": indivURL
    }

    return scrapped_data;