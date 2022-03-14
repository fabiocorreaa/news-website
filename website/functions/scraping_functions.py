from bs4 import BeautifulSoup
import requests


def scrape_apnews():
    html_text = requests.get('https://apnews.com/hub/russia-ukraine?utm_source=apnewsnav&utm_medium=featured').text
    soup = BeautifulSoup(html_text, 'lxml')
    news_title = soup.find_all('h2')
    news_link = soup.find_all('a', {'data-key': 'card-headline'})
    news_desc = soup.find_all('p')
    titles = []
    links = []
    descs = []
    for title, link, desc in zip(news_title, news_link, news_desc):
        titles.append(title.get_text())
        links.append('https://apnews.com' + link.get('href'))
        descs.append(desc.get_text())
    return titles, links, descs


def scrape_g1():
    html_text = requests.get('https://g1.globo.com/tudo-sobre/ucrania/').text
    soup = BeautifulSoup(html_text, 'lxml')
    
    soup.footer.decompose()
    soup.nav.decompose()
    soup.h1.decompose()
    soup.header.decompose()
    news_list = soup.find_all('a')
    titles = []
    links = []
    for news in news_list[:-2]:
        if news.get('href') not in links:
            titles.append(news.get_text())
            links.append(news.get('href'))

    return titles, links


def scrape_bbc():
    html_text = requests.get('https://www.bbc.com/news/world-60525350').text
    soup = BeautifulSoup(html_text, 'lxml')
    news_title = soup.find_all('a', {'class': 'qa-heading-link lx-stream-post__header-link'})
    news_desc = soup.find_all('p', {'class': 'lx-stream-related-story--summary qa-story-summary'})
    titles = []
    links = []
    descs = []
    for line, desc in zip(news_title, news_desc):
        titles.append(line.get_text())
        links.append('https://www.bbc.com' + line.get('href'))
        descs.append(desc.get_text())
    
    return titles, links, descs
    


def scrape_economist():
    html_text = requests.get('https://www.economist.com/ukraine-crisis').text
    soup = BeautifulSoup(html_text, 'lxml')
    news_title = soup.find_all('span', {'class': 'collection-item__headline'})
    news_link = soup.find_all('a', {'class': 'headline-link'})
    news_desc = soup.find_all('p', 'collection-item__description')
    titles = []
    links = []
    descs = []
    for line, link, desc in zip(news_title, news_link, news_desc):
        titles.append(line.get_text())
        if 'https://www.economist.com/' in link.get('href'):
            links.append(link.get('href'))
        else:
            links.append('https://www.economist.com' + link.get('href'))
        descs.append(desc.get_text())
    return titles, links, descs
