## Automatically Capture AQIs Data by Python
Capture the real time AQIs (PM2.5, PM10, etc) through API interface rather than web crawler.  
The script is deployed to the remote Linux server to automatically retrieve data.

## 用python自动获取AQIs数据
通过API接口（而不是爬虫）获取实时AQI气象数据（PM2.5，PM10等），并将该脚本部署到远程Linux服务器上自动获取数据。

## 数据源：pm25.in
该网站每小时更新一次气象数据，指标包括AQI、空气质量、主要污染物、pm2.5、pm10、CO、O3、SO2等。   
API文档详见 http://pm25.in/api_doc
> 声明：本项目提供的数据所有权权归原始方所有，在未获得所有方任何形式认可的情况下，请勿将本数据用作商业目的。本程序提供的数据仅用作参考，不做任何形式的承诺、担保以及负责。

## 文件介绍
``` 
|—— CaptureAQIs.py                      // 核心脚本
|—— AQI.sh                              // 部署在linux上的shell脚本

|—— AQIsData文件夹                      // 数据保存在该文件夹下
    |—— 2018.03.pickle                  // 历史数据
    |—— update.pickle               // 本次更新的数据
    |—— 2018.03.txt                         // 日志文件
    
|—— AQI-Demo文件夹                      //  获取AQI数据的几个小Demo
    |—— Get_AQI_from_aqicn.py
    |—— Get_AQI_from_pm2.5in.py
    |—— GetPmData_Shanghai.py
```
### *CaptureAQIs.py* 
核心代码。用pm25.in官方提供的API获取AQI数据。抓取到的数据保存在pickle文件（以便下一步处理），执行日志保存在[year]-[month].log。
### *AQI.sh*          
部署在linux上，运行CaptureAQIs.py。
### *2018-03.pickle*
获取的AQI数据保存在pickle文件中，以便下一步处理。为防止pickle文件越来越庞大，运行时过分耗费内存，遂将数据**按月存放**。
### update.pickle
本次更新的数据，主要用于下次更新时判断该时段数据是否已更新过
### *2018-03.log*
程序执行时的日志文件。   
通过查看该日志数据抓取状况以及程序运行状况。

----

Raymond Zhang   
2018.3.1
