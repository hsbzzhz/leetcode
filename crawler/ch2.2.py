# -*- coding: utf-8 -*-
"""
Created on 2019-07-03

@author: tony
2.2 赶集网房价数据爬取
"""

import urllib.request
import time
from bs4 import BeautifulSoup

import pandas as pd


# 2、解析数据过程
def parse_HTMLData(htmlstr):
    ''' 解析HTML数据, htmlstr参数是HTML字符串, 返回的解析之后的当前页数据列表 '''
    
    sp = BeautifulSoup(htmlstr, 'html.parser')
    
    # 获得房子信息列表
    # house_list = sp.select('#f_mew_list > div.f-main.f-clear.f-w1190 > div.f-main-left.f-fl.f-w980 > div.f-main-list > div > div')
    house_list = sp.select('#__layout > div > section > section.list-main > section.list-left > section')
    print(len(house_list))
    # 当前页中的记录列表
    page_list = []
    
    for house in house_list:
        
        # 每一行数据
        rows_list = []
        
        # 获得房子信息标题
        # title = house.select('dl > dd.dd-item.title > a')
        title = house.select('div:nth-child(1) > a > div.property-content > div.property-content-detail > div.property-content-title > h3')
        title = title[0].attrs.get('title')
        rows_list.append(title)
        
        # 获得房子信息
        # infos = house.select('dl > dd.dd-item.size > span')
        infos = house.select('div:nth-child(1) > a > div.property-content > div.property-content-detail > section')
        infos = infos[0].text
        detail_data = infos.split('\n')
        # 获得房子户型
        house_type = (detail_data[0]).strip()
        rows_list.append(house_type)
        # 获得房子面积
        house_area = (detail_data[1]).strip()
        rows_list.append(house_area)
         # 获得房子朝向
        house_face = (detail_data[2]).strip()
        rows_list.append(house_face)
         # 获得房子楼层
        house_floor = (detail_data[3]).strip()
        rows_list.append(house_floor)
        
        # 获得房子地址
        address = detail_data[6].strip().split(' ')
        # 获得房子所在城区
        # addr_dist = (detail_data[-1]).split(' ')[-1:]
        rows_list.append(address[-2])
        
        # 获得房子地址所在小区
        # addr_name = house.select('dl > dd.dd-item.address  > span > a > span')
        # addr_name = (addr_name[0].text).strip()
        rows_list.append(address[0])
        
        # 获得房子总价
        price = house.select('div:nth-child(1) > a > div.property-content > div.property-price')
        # total_price = (total_price[0].text).strip()
        price = price[0].text.rsplit(' ', 1)
        total_price = price[0]
        rows_list.append(total_price)
        
        # 获得房子单价
        # price = house.select('div:nth-child(1) > a > div.property-content > div.property-price')
        meter_price = price[-1]
        rows_list.append(meter_price)
                
        page_list.append(rows_list)
    
    return page_list
                     
    

# 1、数据爬取过程
def request_Data(url):
    ''' 爬取当前网页数据, 参数url是当前网页的地址, 返回当前页面数据列表 '''
    
    # 创建Request对象
    req = urllib.request.Request(url)    
    # 数据列表
    page_data_list = []
    
    with urllib.request.urlopen(req) as response:
        # 获得字节序列对象
        data = response.read() 
        htmlstr = data.decode()
        L = parse_HTMLData(htmlstr)
        page_data_list.extend(L)
            
    return page_data_list



# 北京赶集 > 北京房产 > 北京二手房
url_temp = "http://sh.ganji.com/ershoufang/pn{}/"

#最终的列表数据
data_list = []

for i in range(1):
    
    # i是当前页码 
    url = url_temp.format(i)
    print(url)
    print("++++++++++++第{}页++++++++++++++".format(i))
    
    try :        
        # 3、反反爬
        # 休眠5秒
        time.sleep(5)
        L = request_Data(url)
        data_list.extend(L)
    except Exception as e:
        print(e)
        # 3、反反爬
        # 休眠10秒
        time.sleep(10)
        try : 
            L = request_Data(url)
            data_list.extend(L)
            continue
        except Exception as e1:
            print(e1)
        
        # 不再循环
        print('不再有数据结束循环')
        break

print('data_list2 =', len(data_list))
print('爬取数据结束')

# 4、保存数据 
# 列名
colsname = ['标题', '户型', '面积', '朝向', '楼层', '城区', '小区名', '总价', '单价']   

df = pd.DataFrame(data_list, columns=colsname)    
df.to_csv('house_data.csv', index=False, encoding='gbk')

print('保存数据结束')