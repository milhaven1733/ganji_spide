from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random

client=pymongo.MongoClient('localhost',27017)
ganji=client['ganji']
url_list = ganji['url_list2']
item_info = ganji['item_info1']

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Connection':'keep-alive'
}

proxy_list = [
    'http://203.90.144.145',
    'http://124.88.67.14',
    'http://124.88.67.32',
]

proxy_ip=random.choice(proxy_list)
proxies = {'http': proxy_ip}

url='http://bj.ganji.com/ershoubijibendiannao/'

def get_links_from(channel,page):
    list_view='{}o{}'.format(channel,page)
    web_data=requests.get(list_view,headers=headers,proxies=proxies)
    soup=BeautifulSoup(web_data.text,'lxml')
    if soup.find('a','t'):
        links=soup.select('td.t a.t')
        for link in links:
            item_link=link.get('href').split('?')[0]
            print(item_link)
            url_list.insert_one({'url':item_link})
    else:
        pass

#get_links_from(url,2)

def get_item_info_from(url):
    web_data = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find('h1').text=='':
        pass
    else:
        data = {
            'title':soup.find('h1').text,
            'price':soup.select('span.price_now i')[0].text,
            'area':soup.select('div.palce_li > span > i')[0].text.split('-')[1],
            'detail':soup.select('div.baby_kuang.clearfix p')[0].text,
            'url':url
        }
        print(data)
        item_info.insert_one(data)

#get_item_info_from('http://zhuanzhuan.ganji.com/detail/758674428420734979z.shtml')