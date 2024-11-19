#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: Li Haibo
@filename: xy-rgb.py
@Software: PyCharm
@time: 2022/6/15，18：07
@email:
@function：
"""

import pyautogui as pg
import keyboard
import tkinter as tk
import sys
import os
import threading

pg.FAILSAFE = True

mycolor = '#6FB4FF'  # 设置窗口底色
exit_flag = False  # 全局退出标志，用于终止线程


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 图形界面函数
def interface():
    global label_rgb, label_xy, label_hex, label_rp, w, exit_flag
    root = tk.Tk()
    root.title('ScreenPicker')  # 窗口标题
    root.geometry("400x300")  # 窗口大小
    root.configure(bg=mycolor)  # 窗口背景颜色
    root.iconbitmap(resource_path('5a25b454a86f8278880f76336de82e2-迅捷PDF转换器_1.ico'))  # 设置图标

    width, height = pg.size()

    # 设置工作状态显示栏
    tk.Label(root, text='请将鼠标放置指定位置，然后按下CTRL+ALT键！', font=("微软雅黑", 10)).place(x=0, y=10, width=400, height=30)
    tk.Label(root, text='分辨率:', font=("微软雅黑", 10)).place(x=15, y=50, width=70, height=30)
    label_rp = tk.Text(root, font=("微软雅黑", 10), bg='white')
    label_rp.insert("insert", f'***********{width},{height}***********')
    label_rp.place(x=85, y=50, height=30, width=300)

    tk.Label(root, text='坐标:', font=("微软雅黑", 10)).place(x=15, y=100, width=70, height=30)
    label_xy = tk.Text(root, font=("微软雅黑", 10), bg='white')
    label_xy.insert("insert", 'None')
    label_xy.place(x=85, y=100, height=30, width=200)

    tk.Label(root, text='颜色:', font=("微软雅黑", 10)).place(x=15, y=150, width=70, height=30)
    label_rgb = tk.Text(root, font=("微软雅黑", 10), bg='white')
    label_rgb.insert("insert", 'None')
    label_rgb.place(x=85, y=150, height=30, width=200)

    label_hex = tk.Text(root, font=("微软雅黑", 10), bg='white')
    label_hex.insert("insert", 'None')
    label_hex.place(x=85, y=180, height=30, width=200)

    w = tk.Canvas(root, width=80, height=80, bg=mycolor)
    w.config(highlightthickness=0)
    w.place(x=300, y=138)

    tk.Label(root, text='Developer：Li Haibo', font=("微软雅黑", 10)).place(x=0, y=230, width=400, height=26)
    tk.Label(root, text='Email：haibo.li@bjtu.edu.cn', font=("微软雅黑", 10)).place(x=0, y=260, width=400, height=26)

    # 窗口关闭事件
    def on_closing():
        global exit_flag
        exit_flag = True  # 设置退出标志
        root.destroy()  # 销毁窗口

    root.protocol("WM_DELETE_WINDOW", on_closing)  # 绑定关闭窗口事件

    root.mainloop()


# RGB 转换为 Hex
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


# 获取鼠标位置和颜色信息
def run():
    global hex_c, exit_flag
    try:
        while not exit_flag:
            keyboard.wait('ctrl+alt')  # 等待按下 CTRL + ALT 组合键

            x, y = pg.position()  # 获取鼠标位置
            rgb = pg.screenshot().getpixel((x, y))  # 获取颜色

            # 更新 UI
            posi = f'x: {x} y: {y}'
            r, g, b = rgb
            hex_c = rgb2hex(r, g, b)

            # 确保线程安全，使用 Tkinter 的 after 方法更新界面
            label_xy.after(0, lambda: label_xy.delete('1.0', 'end'))
            label_rgb.after(0, lambda: label_rgb.delete('1.0', 'end'))
            label_hex.after(0, lambda: label_hex.delete('1.0', 'end'))

            label_xy.after(0, lambda: label_xy.insert("insert", posi))
            label_rgb.after(0, lambda: label_rgb.insert("insert", f'RGB: {r},{g},{b}'))
            label_hex.after(0, lambda: label_hex.insert("insert", f'Hex: {hex_c}'))
            w.after(0, lambda: w.create_oval(15, 15, 70, 70, fill=hex_c, outline=mycolor))

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        print("退出线程")


if __name__ == '__main__':
    # 创建线程
    t_interface = threading.Thread(target=interface, daemon=True)  # 图形界面线程
    t_run = threading.Thread(target=run, daemon=True)  # 功能逻辑线程

    # 启动线程
    t_interface.start()
    t_run.start()

    # 等待线程结束
    t_interface.join()
