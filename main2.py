from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


urls = [
    'Nihongo Mantappu'
]   

driver = webdriver.Chrome()    
driver.get('https://www.youtube.com/c/{}/videos'.format(urls[0]))
time.sleep(3)
driver.find_element(by=By.XPATH, value='//*[@id="chips"]/yt-chip-cloud-chip-renderer[2]').click()
time.sleep(3)
# content = driver.page_source.encode('utf-8').strip()
videos = driver.find_elements(by=By.CLASS_NAME, value='style-scope ytd-rich-item-renderer')
contents = []

        
for video in videos:
    title = video.find_element(by=By.XPATH, value='.//*[@id="video-title-link"]').text
    view_count = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[1]').text
    link = video.find_element(by=By.XPATH, value='.//*[@id="video-title-link"]').get_attribute('href')
    contents.append({
        'title': title,
        'view_count': view_count,
        'link': link,
    })

df = pd.DataFrame(contents)
print(df)
# driver.close()

  