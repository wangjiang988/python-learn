#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

from Tkinter import *

#function
import display as display


def show(char):
    print('[%s][%s]' % (display.get(), char))
    snum = display.get() + char
    display.set(snum)

def cal():
    try:
        snum = display.get()
        final = eval_r(snum)
        display.set(snum + '=' + str(final))
    except:
        display.set('Error happen!shit!')

def clear():
display.set('')

#data
row = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7]
col = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 2]
txt = ['9', '8', '7', '+', '6', '5', '4', '-', '3', '2', '1', '*', '0', '.', '%', '/', 'clear', '=']
i = 0
colspan = 1
wid = 5

#Tk construct
root = Tk()
root.title('calculator made by DL')
Frame(root)
display = StringVar()

#Label construct
lab = Label(root, relief = 'sunken', borderwidth = 3, anchor = SE)
lab.grid(row = 0, column = 0, columnspan = 4, sticky = SE)
lab.configure(background = 'white', height = 2, width = 25)
lab['textvariable'] = display
lab.bind('<Button-1>', display.set(''))

#Button construct
for i in xrange(0, 18):
    if i < 16:
        cmd = lambda i=i: show(txt[i])
    elif i == 16:
    # cmd = lambda char: clear(char)
        cmd = lambda : clear()
        colspan = 2
        wid = 12
    else:
        # cmd = lambda char: cal(char)
        cmd = lambda : cal()
        bt = Button(root, text = txt[i], width = wid, command = cmd)
        bt.grid(row = row[i], column = col[i], columnspan = colspan)
        # bt.bind('<Button-1>', cmd)

        root.mainloop()