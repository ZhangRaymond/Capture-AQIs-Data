## Capture-AQIs-Data
Capture the real time AQIs (PM2.5, PM10, etc) through API interface rather than web crawler.  
The script is deployed to the remote Linux server to automatically retrieve data.

## 自动获取AQIs数据的python脚本
通过API接口（而不是爬虫）获取实时AQI气象数据（PM2.5，PM10等），并将该脚本部署到远程Linux服务器上自动获取数据。

## 网站介绍

## 文件介绍
### CaptureAQIs.py  
核心代码。request访问
### run.py          
每20分钟运行一次CaptureAQIs.py（以确保不漏掉每次更新）。执行CaptureAQIs.py时如报错中断，则将详细错误信息记录到log.txt中
