# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:43:46 2018

@author: Yemon
"""
import time
import json
import random
import requests

# World Air Quality    http://aqicn.org/
# API doc              http://aqicn.org/json-api/doc/

CityList = {0:'Beijing',1: 'Shanghai'}
Req_City = CityList[0]
Req_Stime = int(round(time.time() * 1000)).__str__()
ip = ''.join([random.randint(1,254).__str__(),'.',random.randint(1,254).__str__(),
                      '.',random.randint(1,254).__str__(),'.',random.randint(1,254).__str__()])
url = ''.join(['http://aqicn.org/aqicn/json/android/',Req_City,'/json?',Req_Stime])
headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                   'X-Forwarded-For': ip}
r = requests.get(url,headers = headers)
data = r.json()

# 该token是我申请的个人token，分享出来
#token = '1b65c6dff11381f5f854d1629c441b5936e1ce1d' 
#url = 'https://api.waqi.info/feed/{}/?token={}'.format(Req_City,token)
## 获取本地气象数据 https://api.waqi.info/feed/here/?token=1b65c6dff11381f5f854d1629c441b5936e1ce1d
#r = requests.get(url,headers = headers)
#Code = r.status_code
#data = r.json()
    
    