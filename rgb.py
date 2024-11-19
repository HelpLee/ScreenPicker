#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Li Haibo
@filename: rgb.py
@Software:PyCharm
@time: 2022/6/15，18：04
@email:20121062@bjtu.edu.cn
@function： 
"""
import pyautogui as pg
import keyboard

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

try:
    width, height = pg.size()
    print(f"Display resolution: {width} * {height}\n")  # 打印屏幕分辨率
    print('按下shift键打印出鼠标所指位置的颜色......')
    while True:
        keyboard.wait('shift')
        x, y = pg.position()
        rgb = pg.screenshot().getpixel((x, y))
        r = str(rgb[0]).rjust(3)
        g = str(rgb[1]).rjust(3)
        b = str(rgb[2]).rjust(3)
        hex_c = rgb2hex(int(r),int(g),int(b))
        color_str = f'选中颜色   RGB:({r},{g},{b}),  16进制:{hex_c}'
        print(color_str)
except KeyboardInterrupt:
    exit('\n\n---- Bye.\n')
