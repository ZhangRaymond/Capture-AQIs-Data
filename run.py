# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:04:15 2018

@author: Yemon
"""



import time
import CaptureAQIs

while True:
      print('Run CaptureAQIs.py')
      try:
            CaptureAQIs.main()
      except Exception as e:
            infor = '[Error] {}'.format(e)
            print(infor)
      seconds = 60*20
      time.sleep(seconds) # 20 minutes
