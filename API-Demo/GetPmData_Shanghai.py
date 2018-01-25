# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:39:31 2018

@author: Raymond Zhang
"""
 
import time
import json
import random
import requests
 
def main():
    Get_PmData()
 
def Convert_Des_Text(aqi_data):
    if aqi_data:
        Pm_Tag = {'0':u'优',
                  '1':u'良',
                  '2':u'轻度污染',
                  '3':u'中度污染',
                  '4':u'重度污染',
                  '5':u'严重污染',
                  '6':u'数据不正常'}
        if (aqi_data >= 0 and aqi_data <= 50):
            Tmp_tag = Pm_Tag['0']
        elif (aqi_data >= 51 and aqi_data <= 100):
            Tmp_tag = Pm_Tag['1']
        elif (aqi_data >= 101 and aqi_data <= 150):
            Tmp_tag = Pm_Tag['2']
        elif (aqi_data >= 151 and aqi_data <= 200):
            Tmp_tag = Pm_Tag['3']
        elif (aqi_data >= 201 and aqi_data <= 300):
            Tmp_tag = Pm_Tag['4']
        elif (aqi_data >= 300):
            Tmp_tag = Pm_Tag['5']
        else:
            Tmp_tag = Pm_Tag['6']
    return Tmp_tag
 
def Get_PmData():
    try:
        Pm_Json_Data = Get_AmericanEmbassy_PmData()
        Convert_AmericanEmbassy_Data(Pm_Json_Data)
    except:
        Pm_Json_Data = Get_China_PmData()
        Convert_China_Data(Pm_Json_Data)
 
def Get_China_PmData():
    City_list = {'0':'beijing','1': 'shanghai'}
    Req_City = City_list['1']
    Req_Token = '5j1znBVAsnSf5xQyNQyq'
    Req_Ip = ''.join([random.randint(1,254).__str__(),'.',random.randint(1,254).__str__(),'.',random.randint(1,254).__str__(),'.',random.randint(1,254).__str__()])
    Req_Url = ''.join(['http://www.pm25.in/api/querys/pm2_5.json?city=',Req_City,'&token=',Req_Token])
    Req_headers = {'content-type': 'application/json; charset=utf-8',
                   'User-Agent': 'python-requests/2.14.2 python/3.6.1 Windows/10',
                   'X-Forwarded-For': Req_Ip}
    Request_Result = requests.get(Req_Url,headers=Req_headers)
    Request_Code = Request_Result.status_code
    Request_Content = Request_Result.text
    return Request_Content
 
def Convert_China_Data(json_data):
    if json_data:
        Load_Json_Data = json.loads(json_data)
        Check_Site_Length = Load_Json_Data.__len__()
        print(Load_Json_Data[0]["time_point"])
        for i in range(Check_Site_Length):
            Pm_Tag_Data = int(Load_Json_Data[i]["aqi"])
            Tmp_tag = Convert_Des_Text(Pm_Tag_Data)
            print(Load_Json_Data[i]["position_name"],u'AQI:',Load_Json_Data[i]["aqi"],Tmp_tag)
 
def Get_AmericanEmbassy_PmData():
    City_list = {'0':'Beijing','1': 'Shanghai'}
    Req_City = City_list['1']
    Req_Stime = int(round(time.time() * 1000)).__str__()
    Req_Ip = ''.join([random.randint(1,254).__str__(),'.',random.randint(1,254).__str__(),
                      '.',random.randint(1,254).__str__(),'.',random.randint(1,254).__str__()])
    Req_Url = ''.join(['http://aqicn.org/aqicn/json/android/',Req_City,'/json?',Req_Stime])
    Req_headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                   'X-Forwarded-For': Req_Ip}
    Request_Result = requests.get(Req_Url,headers=Req_headers)
    Request_Code = Request_Result.status_code
    Request_Content = Request_Result.text
    return Request_Content
 
def Convert_AmericanEmbassy_Data(json_data):
    if json_data:
        Load_Json_Data = json.loads(json_data)
        #print Load_Json_Data["nearest"][0]["pol"]
        print(u'时间:',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(Load_Json_Data["time"])),
              u'AQI:',Load_Json_Data["aqi"])
        Check_Site_Length = Load_Json_Data["nearest"].__len__()
        for i in range(Check_Site_Length):
            Pm_Tag_Data = int(Load_Json_Data["nearest"][i]["v"])
            Tmp_tag = Convert_Des_Text(Pm_Tag_Data)
            print(Load_Json_Data["nearest"][i]["nna"],Load_Json_Data["nearest"][i]["v"],Tmp_tag)
 
if __name__ == '__main__':
    main()