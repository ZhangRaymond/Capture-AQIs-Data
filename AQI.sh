#!/bin/sh

# 安装python包
# python3.6 -m pip install numpy scipy pandas requests sklearn

# 进入CaptureAQIs.py所在目录
cd /home/Ben/AQI
# cd "$( dirname "${BASH_SOURCE[0]}" )" && 
python3.6 ./CaptureAQIs.py

