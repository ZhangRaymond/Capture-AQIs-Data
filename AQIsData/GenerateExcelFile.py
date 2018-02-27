# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:38:13 2018

@author: Yemon
"""

import pandas as pd
his = pd.read_pickle('history-2018-02.pickle')   # [Full_his, City_his, time_his]
update = pd.read_pickle('thisUpdate.pickle') # [Full_stations, City_only, time_point]

def write_to_Excel(data):
      Full_stations,City_only = update
      Full_his,City_his,time_his = his
      
      writer = pd.ExcelWriter('update-AQIs-data.xlsx')
      Full_stations.to_excel(writer, sheet_name ='This Update(Full Stations)')
      City_only.to_excel(writer, sheet_name ='This Update(City Only)')
      writer.save()
#      print('                Sucessfully update the [update AQIs data.xlsx]!')

      writer = pd.ExcelWriter('history-AQIs-data.xlsx')
      Full_his.to_excel(writer, sheet_name ='All Stations')
      City_his.to_excel(writer, sheet_name ='City Only')
      time_his.to_excel(writer, sheet_name ='Update Log')
      writer.save()
#      print('                Sucessfully update the [history AQIs data.xlsx]!')