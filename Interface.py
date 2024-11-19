#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Li Haibo
@filename: Interface.py
@Software:PyCharm
@time: 2022/6/15，22：58
@email:20121062@bjtu.edu.cn
@function： 
"""

import tkinter as tk
root = tk.Tk()
root.title('色彩坐标提取器 V1.0')  # 给窗口取名
root.geometry("320x180")
mycolor = '#6FB4FF'  # 设置窗口底色
root.configure(bg=mycolor)

# 设置工作状态显示栏
tk.Label(root, text='请将鼠标放置指定位置，然后按下CTRL键！', ).place(x=40, y=10, width=240, height=26)
tk.Label(root, text='坐标:', ).place(x=15, y=50, width=60, height=26)
label_xy = tk.Label(root, text='请将鼠标放置指定位置！', font=("华文行楷", 15), bg='white')
label_xy.place(x=75, y=50, height=26, width=230)

tk.Label(root, text='颜色:', ).place(x=15, y=100, width=60, height=26)
label_rgb = tk.Label(root, text='软件已开始运行！', font=("华文行楷", 15), bg='white')
label_rgb.place(x=70, y=100, height=26, width=230)

# 大循环
root.after(250)
root.mainloop()