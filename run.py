# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:04:15 2018

@author: Yemon
"""



import time
import traceback
import CaptureAQIs

# log in log.txt
CaptureAQIs.log('--------------------')
CaptureAQIs.log('Manually Run run.py')
CaptureAQIs.log('--------------------')

while True:
      print('Run CaptureAQIs.py')
      try:
            CaptureAQIs.main()
      except Exception:
            CaptureAQIs.log('[Error] \n{}'.format(traceback.format_exc()))
      seconds = 60*20
      time.sleep(seconds) # 20 minutes
