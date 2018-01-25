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
            _,_,time_point = pd.read_pickle('update.pickle')
      except:
            time_point = ''
      return time_point

def download_data(CityList):
      previous_time_point = previous_time()
      Full_stations = City_only = pd.DataFrame()
      url = 'http://www.pm25.in/api/querys/aqi_details.json'
      #url = 'http://www.pm25.in/api/querys/all_cities.json'
      token = '5j1znBVAsnSf5xQyNQyq'
      for i in range(len(CityList)):
            city = CityList[i]
#            print(' loading: {}'.format(city))
            param  = {'city':city,'token':token}
            r = requests.get(url, params = param)
            code = r.status_code
            
            #判断是否通信成功
            if code == 200:
      #            print('       GET request ok')
                  content = r.json()
                  # 获取此次更新的时间： 选择最后一条（for city），以免某些废站点的数据误导
                  if isinstance(content, dict):
                        infor = '[Failed]   token of API is out of use. Take a break'
                        UPDATE = False
                        return [UPDATE,infor]
                  elif isinstance(content, list):
                        time_point = content[-1]['time_point'] 
                        # 判断是否与上次获取数据的time_point,相同则取消此次更新
                        if time_point == previous_time_point:
                              infor = '[Canceled] Same as the previous time point, so this update has been canceled!'
#                              print(infor)
                              UPDATE = False
                              return [UPDATE,infor]
                        else:
                              city_data = pd.DataFrame(content).fillna('')
                              Full_stations = Full_stations.append(city_data, ignore_index=True)
                              City_only = City_only.append(city_data.iloc[-1], ignore_index=True)
                              if i == len(CityList)-1:
                                    infor ='[Success]  Updated all cities! TimePoint: {}'.format(str(time_point))
#                                    print(infor)
                                    UPDATE = True
                                    return [UPDATE,infor,Full_stations,City_only]
            else:
                  UPDATE = False
                  infor = '[Error]    GET request error ({})'.format(code)
#                  print('    ',infor)
                  return [UPDATE,infor]
                 


def updata_to_pickle(data):
      Full_stations,City_only = data
      # 改变列顺序，使之更易读
      columns = ['time_point','area','position_name','station_code','aqi','quality',
           'primary_pollutant','pm2_5', 'pm2_5_24h','pm10', 'pm10_24h',
           'co', 'co_24h', 'no2', 'no2_24h', 'o3', 'o3_24h', 
           'o3_8h', 'o3_8h_24h','so2', 'so2_24h']
      Full_stations = Full_stations.reindex_axis(columns, axis=1)
      City_only = City_only.reindex_axis(columns, axis=1)
      City_only.pop('position_name')
      City_only.pop('station_code')
      time_point = City_only.iloc[0,0]
#      time_point = City_only.ix[0,'time_point']
      
      # 保存此次update的数据
      with open('update.pickle', 'wb') as file:
            pickle.dump([Full_stations, City_only, time_point], file)
            
      # 将更新并入历史数据并保存
      try:
            Full_his, City_his,time_his = pd.read_pickle('History.pickle')
      except Exception as e:
            print(e)
            Full_his = City_his = pd.DataFrame()
            time_his = pd.Series()
            print('                Fail to load [History.pickle], create new empty history data!')
      
      Full_his = pd.concat([Full_stations, Full_his], axis=0, join='outer', ignore_index=True)
      City_his = pd.concat([City_only, City_his], axis=0, join='outer', ignore_index=True)
      time_his = pd.Series(time_point).append(time_his,ignore_index=True)
      with open('History.pickle', 'wb') as file:
            pickle.dump([Full_his, City_his, time_his], file)
      return [Full_stations,City_only,Full_his,City_his,time_his]

def write_to_Excel(data):
      Full_stations,City_only,Full_his,City_his,time_his = data
      
      writer = pd.ExcelWriter(r'../update-AQIs-data.xlsx')
      Full_stations.to_excel(writer, sheet_name ='This Update(Full Stations)')
      City_only.to_excel(writer, sheet_name ='This Update(City Only)')
      writer.save()
#      print('                Sucessfully update the [update AQIs data.xlsx]!')

      writer = pd.ExcelWriter(r'../history-AQIs-data.xlsx')
      Full_his.to_excel(writer, sheet_name ='All Stations')
      City_his.to_excel(writer, sheet_name ='City Only')
      time_his.to_excel(writer, sheet_name ='Update Log')
      writer.save()
#      print('                Sucessfully update the [history AQIs data.xlsx]!')

def log(infor):
      with open(r'../log.txt', 'r') as f:
            content = f.readlines()[2:]
      with open(r'../log.txt', 'w') as f:
            head = '     Log Time       | Informaiton\n'
            now = str(datetime.datetime.now())[:-7]
            update = '\n{} | {}\n'.format(now,infor)
            print(update)
            f.write(head+update)   
            f.writelines(content)
      
      

def main():
      CityList = {0:'guangzhou',1:'zhaoqing',2:'foshan',3:'huizhou',4:'dongguan',
                  5:'zhongshan',6:'shenzhen',7:'jiangmen',8:'zhuhai'}
      
      value = download_data(CityList)
      UPDATE = value[0]
      infor = value[1]
      if UPDATE:
            try:
                  data = updata_to_pickle(value[2:])
                  write_to_Excel(data)
            except Exception as e:
                  infor = '[Failed]   Sucessfully downloaded, but fail to write into pickle and Excel file!'\
                          '\n                               {}'.format(e)
      log(infor)
      
            
if __name__ == '__main__':
      main()
      
      