#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Lee HaiBo
@filename: mouse.py
@Software:PyCharm
@time: 2021/9/4，22：51
@email:lntulhb@163.com
@function： 
"""
import pyautogui
import time
pyautogui.FAILSAFE = True
try:
    while True:
        x,y = pyautogui.position()
        posi = 'x:' + str(x).rjust(4) + ' y:' + str(y).rjust(4)
        print('\r',posi,end='')
        time.sleep(0.5)

except KeyboardInterrupt:
    print('已退出！')
