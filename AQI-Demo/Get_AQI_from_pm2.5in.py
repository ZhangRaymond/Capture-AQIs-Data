# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:51:37 2018

@author: Raymond Zhang
"""
import random
import requests
import pandas as pd


# Reference： http://www.pm25.in/api_doc


# 生成伪IP
ip = ''.join([random.randint(1,254).__str__(),'.',
              random.randint(1,254).__str__(),'.',
              random.randint(1,254).__str__(),'.',
              random.randint(1,254).__str__()])
# toekn：该api接口的要求，公共测试接口，进一步使用需单独申请
token = '5j1znBVAsnSf5xQyNQyq'
# url参数： Requests 包会自动加入url中
CityList = {0:'beijing',1:'shanghai',2:'guangzhou',3:'huhehaote'}
param  = {'city':CityList[2], 'token':token}
url = 'http://www.pm25.in/api/querys/aqi_details.json'
#url = 'http://www.pm25.in/api/querys/aqi_details.json?city=beijing&token=5j1znBVAsnSf5xQyNQyq'
# 自定义请求头（如需）
headers = {'content-type': 'application/json',
           'User-Agent': 'python-requests/2.14.2 python/3.6.1 Windows/10',
           'X-Forwarded-For': ip}
# 调用GET功能获取API返回值——即服务器返回的气象数据
r = requests.get(url, params = param, headers = headers)
Code = r.status_code # 200(正常)/404/403等
Data_dic = r.json()  # requests包自带json解包，无需调用json.loads(r.text)



# 打印部分信息
if isinstance(Data_dic, dict):
      print('\n',Data_dic['error'])
elif isinstance(Data_dic, list):
      print('\n',Data_dic[0]["time_point"],'\n')
      for pointData in Data_dic:
            aqi = pointData["aqi"]
            print(pointData["position_name"],u'AQI:',pointData["aqi"],pointData['quality'])
      Data_df = pd.DataFrame(Data_dic).fillna('')


#Content = '[{"aqi":139,"area":"广州","pm2_5":106,"pm2_5_24h":140,"position_name":"广雅中学","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1345A","time_point":"2018-01-21T17:00:00Z"},{"aqi":135,"area":"广州","pm2_5":103,"pm2_5_24h":119,"position_name":"市五中","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1346A","time_point":"2018-01-21T17:00:00Z"},{"aqi":0,"area":"广州","pm2_5":0,"pm2_5_24h":0,"position_name":"天河职幼","primary_pollutant":null,"quality":null,"station_code":"1347A","time_point":"2015-06-01T14:00:00Z"},{"aqi":108,"area":"广州","pm2_5":81,"pm2_5_24h":101,"position_name":"广东商学院","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1348A","time_point":"2018-01-21T17:00:00Z"},{"aqi":119,"area":"广州","pm2_5":90,"pm2_5_24h":104,"position_name":"市八十六中","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1349A","time_point":"2018-01-21T17:00:00Z"},{"aqi":108,"area":"广州","pm2_5":81,"pm2_5_24h":88,"position_name":"番禺中学","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1350A","time_point":"2018-01-21T17:00:00Z"},{"aqi":156,"area":"广州","pm2_5":119,"pm2_5_24h":157,"position_name":"花都师范","primary_pollutant":"细颗粒物(PM2.5)","quality":"中度污染","station_code":"1351A","time_point":"2018-01-21T17:00:00Z"},{"aqi":125,"area":"广州","pm2_5":95,"pm2_5_24h":129,"position_name":"市监测站","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1352A","time_point":"2018-01-21T17:00:00Z"},{"aqi":150,"area":"广州","pm2_5":115,"pm2_5_24h":93,"position_name":"九龙镇镇龙","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1353A","time_point":"2018-01-21T17:00:00Z"},{"aqi":144,"area":"广州","pm2_5":110,"pm2_5_24h":137,"position_name":"麓湖","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"1354A","time_point":"2018-01-21T17:00:00Z"},{"aqi":169,"area":"广州","pm2_5":128,"pm2_5_24h":139,"position_name":"帽峰山森林公园","primary_pollutant":"细颗粒物(PM2.5)","quality":"中度污染","station_code":"1355A","time_point":"2018-01-21T17:00:00Z"},{"aqi":103,"area":"广州","pm2_5":77,"pm2_5_24h":84,"position_name":"体育西","primary_pollutant":"细颗粒物(PM2.5)","quality":"轻度污染","station_code":"2846A","time_point":"2018-01-21T17:00:00Z"},{"aqi":132,"area":"广州","pm2_5":100,"pm2_5_24h":117,"position_name":null,"primary_pollutant":"颗粒物(PM2.5)","quality":"轻度污染","station_code":null,"time_point":"2018-01-21T17:00:00Z"}]'
#Content = '[{"aqi":57,"area":"上海","pm2_5":31,"pm2_5_24h":59,"position_name":"十五厂","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1142A","time_point":"2018-01-21T16:00:00Z"},{"aqi":58,"area":"上海","pm2_5":41,"pm2_5_24h":60,"position_name":"虹口","primary_pollutant":"细颗粒物(PM2.5)","quality":"良","station_code":"1143A","time_point":"2018-01-21T16:00:00Z"},{"aqi":54,"area":"上海","pm2_5":37,"pm2_5_24h":60,"position_name":"徐汇上师大","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1144A","time_point":"2018-01-21T16:00:00Z"},{"aqi":57,"area":"上海","pm2_5":36,"pm2_5_24h":58,"position_name":"杨浦四漂","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1145A","time_point":"2018-01-21T16:00:00Z"},{"aqi":68,"area":"上海","pm2_5":49,"pm2_5_24h":79,"position_name":"青浦淀山湖","primary_pollutant":"细颗粒物(PM2.5)","quality":"良","station_code":"1146A","time_point":"2018-01-21T16:00:00Z"},{"aqi":56,"area":"上海","pm2_5":38,"pm2_5_24h":61,"position_name":"静安监测站","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1147A","time_point":"2018-01-21T16:00:00Z"},{"aqi":60,"area":"上海","pm2_5":37,"pm2_5_24h":48,"position_name":"浦东川沙","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1148A","time_point":"2018-01-21T16:00:00Z"},{"aqi":54,"area":"上海","pm2_5":32,"pm2_5_24h":56,"position_name":"浦东新区监测站","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1149A","time_point":"2018-01-21T16:00:00Z"},{"aqi":65,"area":"上海","pm2_5":33,"pm2_5_24h":54,"position_name":"浦东张江","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1150A","time_point":"2018-01-21T16:00:00Z"},{"aqi":64,"area":"上海","pm2_5":33,"pm2_5_24h":64,"position_name":"普陀","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1141A","time_point":"2018-01-21T16:00:00Z"},{"aqi":59,"area":"上海","pm2_5":36,"pm2_5_24h":59,"position_name":null,"primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":null,"time_point":"2018-01-21T16:00:00Z"}]'
#Content = '[{"aqi":67,"area":"北京","pm2_5":30,"pm2_5_24h":26,"position_name":"万寿西宫","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1001A","time_point":"2018-01-21T17:00:00Z"},{"aqi":70,"area":"北京","pm2_5":47,"pm2_5_24h":40,"position_name":"定陵","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1002A","time_point":"2018-01-21T17:00:00Z"},{"aqi":70,"area":"北京","pm2_5":41,"pm2_5_24h":33,"position_name":"东四","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1003A","time_point":"2018-01-21T17:00:00Z"},{"aqi":66,"area":"北京","pm2_5":36,"pm2_5_24h":30,"position_name":"天坛","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1004A","time_point":"2018-01-21T17:00:00Z"},{"aqi":80,"area":"北京","pm2_5":59,"pm2_5_24h":35,"position_name":"农展馆","primary_pollutant":"细颗粒物(PM2.5)","quality":"良","station_code":"1005A","time_point":"2018-01-21T17:00:00Z"},{"aqi":69,"area":"北京","pm2_5":37,"pm2_5_24h":28,"position_name":"官园","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1006A","time_point":"2018-01-21T17:00:00Z"},{"aqi":78,"area":"北京","pm2_5":41,"pm2_5_24h":29,"position_name":"海淀区万柳","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1007A","time_point":"2018-01-21T17:00:00Z"},{"aqi":73,"area":"北京","pm2_5":51,"pm2_5_24h":41,"position_name":"顺义新城","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1008A","time_point":"2018-01-21T17:00:00Z"},{"aqi":69,"area":"北京","pm2_5":44,"pm2_5_24h":38,"position_name":"怀柔镇","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1009A","time_point":"2018-01-21T17:00:00Z"},{"aqi":76,"area":"北京","pm2_5":47,"pm2_5_24h":38,"position_name":"昌平镇","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1010A","time_point":"2018-01-21T17:00:00Z"},{"aqi":71,"area":"北京","pm2_5":39,"pm2_5_24h":32,"position_name":"奥体中心","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1011A","time_point":"2018-01-21T17:00:00Z"},{"aqi":62,"area":"北京","pm2_5":44,"pm2_5_24h":31,"position_name":"古城","primary_pollutant":"颗粒物(PM10),细颗粒物(PM2.5)","quality":"良","station_code":"1012A","time_point":"2018-01-21T17:00:00Z"},{"aqi":71,"area":"北京","pm2_5":43,"pm2_5_24h":33,"position_name":null,"primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":null,"time_point":"2018-01-21T17:00:00Z"}]'
#Content = '[{"aqi":98,"area":"呼和浩特","pm2_5":44,"pm2_5_24h":62,"position_name":"呼市一监","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1090A","time_point":"2018-01-21T17:00:00Z"},{"aqi":95,"area":"呼和浩特","pm2_5":43,"pm2_5_24h":40,"position_name":"小召","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1091A","time_point":"2018-01-21T17:00:00Z"},{"aqi":78,"area":"呼和浩特","pm2_5":39,"pm2_5_24h":29,"position_name":"兴松小区","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1092A","time_point":"2018-01-21T17:00:00Z"},{"aqi":84,"area":"呼和浩特","pm2_5":49,"pm2_5_24h":53,"position_name":"糖厂","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1093A","time_point":"2018-01-21T17:00:00Z"},{"aqi":86,"area":"呼和浩特","pm2_5":44,"pm2_5_24h":37,"position_name":"如意水处理厂","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1094A","time_point":"2018-01-21T17:00:00Z"},{"aqi":93,"area":"呼和浩特","pm2_5":46,"pm2_5_24h":35,"position_name":"二十九中","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1095A","time_point":"2018-01-21T17:00:00Z"},{"aqi":95,"area":"呼和浩特","pm2_5":68,"pm2_5_24h":51,"position_name":"工大金川校区","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1096A","time_point":"2018-01-21T17:00:00Z"},{"aqi":98,"area":"呼和浩特","pm2_5":60,"pm2_5_24h":57,"position_name":"化肥厂生活区","primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":"1097A","time_point":"2018-01-21T17:00:00Z"},{"aqi":92,"area":"呼和浩特","pm2_5":49,"pm2_5_24h":45,"position_name":null,"primary_pollutant":"颗粒物(PM10)","quality":"良","station_code":null,"time_point":"2018-01-21T17:00:00Z"}]'

