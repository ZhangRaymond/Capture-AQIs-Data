# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:38:13 2018

@author: Yemon
"""

import pandas as pd
import os

def check_file(file):
      if os.path.exists(file):
            i = input('{} 已存在！ \n继续生成将覆盖原文件，是否继续? [y]/n  '.format(file))
      else:
            i = 'y'
      return i

def write_to_Excel(his,update,pickle_his,pickle_update):
      Full_stations,City_only,time_point = update
      Full_his,City_his,time_his = his
      
      xlsx_update = pickle_update[:-7] + '.xlsx'  #更换后缀
      xlsx_his = pickle_his[:-7] + '.xlsx'
      
      
      i = check_file(xlsx_update)
      if i.lower() == 'n':
            print('已跳过')
      else:
            writer = pd.ExcelWriter(xlsx_update)
            Full_stations.to_excel(writer, sheet_name ='All Stations')
            City_only.to_excel(writer, sheet_name ='City Only')
            writer.save()
            print('已生成 {}  (from {})'.format(xlsx_update,pickle_update))
      
      i = check_file(xlsx_his)
      if i.lower() == 'n':
            print('已跳过')
      else:
            print('Creating...... '.format(xlsx_update))
            writer = pd.ExcelWriter(xlsx_his)
            Full_his.to_excel(writer, sheet_name ='All Stations')
            City_his.to_excel(writer, sheet_name ='City Only')
            time_his.to_excel(writer, sheet_name ='Update Log')
            writer.save()
            print('已生成 {}  (from {})'.format(xlsx_his,pickle_his))

            
file_his = 'history-2018-02.pickle'
file_update = 'thisUpdate.pickle'

his = pd.read_pickle(file_his)   # [Full_his, City_his, time_his]
update = pd.read_pickle(file_update) # [Full_stations, City_only, time_point]

write_to_Excel(his,update,file_his,file_update)

