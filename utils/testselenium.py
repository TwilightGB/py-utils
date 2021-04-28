import os
import time

from bs4 import BeautifulSoup
from pip._vendor import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome('../data/chromedriver')
    # driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    driver.get('https://www.toutiao.com/a6950619776863453704/')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    tturls = soup.body.select('img[src]')
    for img_tag in tturls:
        imgurl = img_tag.attrs['src']
        saveimg(imgurl)
        print(img_tag.attrs['src'])
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def saveimg(img_url):
    name=str(img_url).split("/")[-1]
    if str(img_url).startswith("http"):
        savepath = mklocation()
        try:
            get_img = requests.get(img_url, allow_redirects=True).content
            with open(savepath+name,'wb') as fp:
                fp.write(get_img)

        except:
            print('error: '+ img_url)


def mklocation():
    pathdir = time.strftime("%Y-%m-%d-%H", time.localtime());
    savepath = '/Users/gengbin/Downloads/img/' + pathdir + "/"
    isExists = os.path.exists(savepath)
    if not isExists:
        os.makedirs(savepath)
    return savepath


if __name__ == '__main__':
    main()