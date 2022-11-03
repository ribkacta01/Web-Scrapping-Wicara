from selenium import webdriver 
from bs4 import BeautifulSoup

urls = [
    'CBSNews'
]


def main():
    driver = webdriver.Chrome()
    for url in urls:
        driver.get('https://www.youtube.com/c/{}/videos'.format(urls[0]))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a',id='video-title-link')
        views = soup.findAll('span',class_='style-scope ytd-rich-grid-media')
        video_urls = soup.findAll('a',id='video-title-link')
        print('Channel: https://www.youtube.com/{}'.format(*{urls[0]}))
        i = 0 # view and time 
        j = 0 # urls
        for title in titles[:10]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
            i+=2
            j+=1
main()           