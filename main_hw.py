from multiprocessing import Pool
from channel import channel_list
from page import get_links_from,get_item_info_from,url_list,item_info

def get_all_links_from(channel):
    for i in range(1,51):
        get_links_from(channel,i)

def test_pool(item):
    try:
        print(item['url'])
        get_item_info_from(item['url'])
    except KeyError:
        pass

if __name__=='__main__':
    # pool=Pool(processes=4)
    # pool.map(get_all_links_from,channel_list.split())
    # pool.close()
    # pool.join()

    # pool2=Pool(processes=4)
    # pool2.map(test_pool,url_list.find())
    k=0
    for i in item_info.find():
        print(i['area'])
        print(k)
        k+=1