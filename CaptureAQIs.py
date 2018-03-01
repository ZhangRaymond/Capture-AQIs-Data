# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:34:19 2018
@author: Raymond Zhang

主要功能： 从pm2.5in官网API接口获取实时气象数据，并写入Excel文件

API doc： http://www.pm25.in/api_doc

"""

import requests
import pandas as pd
import pickle
import datetime

def previous_time():
      try:
            _,_,time_point = pd.read_pickle('AQIsData/thisUpdate.pickle')
      except:
            time_point = ''
      return time_point

def download_data(CityList):
      previous_time_point = previous_time()
      Full_stations = City_only = pd.DataFrame()
      url = 'http://www.pm25.in/api/querys/aqi_details.json'
      #url = 'http://www.pm25.in/api/querys/all_cities.json'
      token = '5j1znBVAsnSf5xQyNQyq'
      header = {'content-type': 'application/json; charset=utf-8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                  'Connection': 'close'}
      ErrorCities = [] # 由于网络等原因未能下载到数据的城市，记录之并稍后再次访问
      for i in range(len(CityList)):
            city = CityList[i]
#            print(' loading: {}'.format(city))
            param  = {'city':city,'token':token}
            try:
                r = requests.get(url, params = param,headers=header,timeout=5)
            except Exception as e:
                ErrorCities.append(city) 
                log('[Request Error]  City: [{}] is unable to download. \n{}'.format(city,e))
                continue
            code = r.status_code
            #判断是否通信成功
            if code == 200:
#                  log('GET request OK： {}'.format(city))
                  content = r.json()
                  if isinstance(content, dict):
                        log('[Failed]   token of API is out of use: {}'.format(city))
                        return
                  elif isinstance(content, list):
                        # 获取此次更新的时间： 选择最后一条（for city），以免某些废站点的数据误导
                        time_point = content[-1]['time_point'] 
                        # 判断是否与上次获取数据的time_point,相同则取消此次更新
                        if time_point == previous_time_point:
                              log('[Canceled] Same as the previous')
                              return
                        else:
                              city_data = pd.DataFrame(content).fillna('')
                              Full_stations = Full_stations.append(city_data, ignore_index=True)
                              City_only = City_only.append(city_data.iloc[-1], ignore_index=True)
            else:
                  ErrorCities.append(city) 
                  log('[Error]    GET request error {}: {}'.format(code,city))
            
      if len(ErrorCities)>0:
            error_cities = ''
            for city in ErrorCities:
                  error_cities = error_cities + ' ' + city
            log('           The following cities are not updated: {}'.format(error_cities))
            infor = '[Success]  Updated some of cities! TimePoint: {}'.format(str(time_point))
      elif len(ErrorCities)==0:
            infor = '[Success]  Updated all cities!     TimePoint: {}'.format(str(time_point))
      return [infor,[Full_stations,City_only]]
      
                 
def update_to_pickle(data):
      Full_stations,City_only = data
      # 改变列顺序，使之更易读
      columns = ['time_point','area','position_name','station_code','aqi','quality',
           'primary_pollutant','pm2_5', 'pm2_5_24h','pm10', 'pm10_24h',
           'co', 'co_24h', 'no2', 'no2_24h', 'o3', 'o3_24h', 
           'o3_8h', 'o3_8h_24h','so2', 'so2_24h']
      Full_stations = Full_stations.reindex(columns=columns)
      City_only = City_only.reindex(columns=columns)
      City_only.pop('position_name')
      City_only.pop('station_code')
      time_point = City_only.iloc[0,0]
#      time_point = City_only.ix[0,'time_point']
      
      # 保存此次update的数据
      with open('AQIsData/thisUpdate.pickle', 'wb') as file:
            pickle.dump([Full_stations, City_only, time_point], file)
            
      # 将更新并入历史数据
      month = time_point[:7]
      his_filename = 'history-{}.pickle'.format(month)
      filepath = 'AQIsData/'+his_filename
      import os
      if os.path.exists(filepath):
            try:
                  Full_his, City_his, time_his = pd.read_pickle(filepath)
            except Exception as e:
                  # 如无法获取该月份的历史数据，为了避免覆写历史数据的误操作，将本次更新的数据另建一pickle，以待后续手动合并
                  filename = 'not-merged-Data-{}.pickle'.format(time_point)
                  with open('AQIsData/'+filename, 'wb') as file:
                        pickle.dump([Full_stations, City_only, time_point], file)
                  log('[Error]  Fail to load [{}] and unable to merge into his data. \
                                     Create an extra file:{}.  ({})'.format(his_filename,filename,e))
                  return 
      else:
            #否则新建新月份的pickle文件
            Full_his = City_his = pd.DataFrame()
            time_his = pd.Series()
            log('=======================================================================================')
            log('[New his pickle] Create {}'.format(his_filename))
      #合并
      Full_his = pd.concat([Full_stations, Full_his], axis=0, join='outer', ignore_index=True)
      City_his = pd.concat([City_only, City_his], axis=0, join='outer', ignore_index=True)
      time_his = pd.Series(time_point).append(time_his,ignore_index=True)
      with open(filepath, 'wb') as file:
            pickle.dump([Full_his, City_his, time_his], file)

def log(infor):
      #filepath = r'AQIsData/'+filename
      filepath = r'AQIsData/log.txt'
      try:
            with open(filepath, 'r') as f:
                  content = f.readlines()[2:]
      except:
            content = ''
      with open(filepath, 'w') as f:
            head = '     Log Time       | Informaiton\n\n'
            now = str(datetime.datetime.now())[:-7]
            update = '{} | {}\n'.format(now,infor)
            print(update)
            f.write(head+update)   
            f.writelines(content)

      
def main():
      CityList = {0:'guangzhou',1:'zhaoqing',2:'foshan',3:'huizhou',4:'dongguan',
                  5:'zhongshan',6:'shenzhen',7:'jiangmen',8:'zhuhai'}
      
      data = download_data(CityList)
      
      # update
      if data!=None:
            update_to_pickle(data[1])
            infor = data[0]
            log(infor)
            
      
if __name__ == '__main__':
      main()
      
      