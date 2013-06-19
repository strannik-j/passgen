#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  passgen-gui.py
#
#  Copyright 2012 Strannik-j <mail@strannik-j.org>
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the Strannik Foundation nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  * All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#
#     This product includes software developed by a Strannik-j
#     and his contributors.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
from tkinter import *
from passgen import generate

root = Tk(screenName=None, className='PassGen')
frame0 = Frame(root, width=100, height=100)


ent_text_len = StringVar()
ent_text_pass = IntVar()


var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

var0.set(1)
var1.set(1)
var2.set(1)
var3.set(0)
ent_text_len.set(6)
ent_text_pass.set('')

password = StringVar()


def main():

    return 0


def gen(event):
    vpa, vpA, vp0, vpx = 0, 0, 0, 0

    var_len = int(ent_text_len.get())
    password = ''
    if var0.get() == 1:
        vpa = 1
    if var1.get() == 1:
        vpA = 1
    if var2.get() == 1:
        vp0 = 1
    if var3.get() == 1:
        vpx = 1
    password = generate(var_len, vpa, vpA, vp0, vpx)
    ent_text_pass.set(password)
    print(password)
    return 0


def _exit(event):
    sys.exit()


but_gen = Button(frame0, text="Generate", width=7)
but_gen.bind("<Button-1>", gen)
but_exit = Button(frame0, text='Exit', width=4)
but_exit.bind("<Button-1>", _exit)


cbut0 = Checkbutton(frame0, text="abc", variable=var0, onvalue=1, offvalue=0)
cbut1 = Checkbutton(frame0, text="ABC", variable=var1, onvalue=1, offvalue=0)
cbut2 = Checkbutton(frame0, text="012", variable=var2, onvalue=1, offvalue=0)
cbut3 = Checkbutton(frame0, text="!@#", variable=var3, onvalue=1, offvalue=0)


ent0 = Entry(frame0, width=5, bd=3, textvariable=ent_text_len)
ent1 = Entry(frame0, width=22, bd=3, textvariable=ent_text_pass)


lab0 = Label(frame0, width=10, text="Длинна:", font="Sans 12")
lab1 = Label(frame0, width=10, text="Символы:", font="Sans 12")
lab2 = Label(frame0, width=10, text="Пароль:", font="Sans 12")


frame0.grid(row=0, column=0)
lab0.grid(row=0, column=0)
ent0.grid(row=0, column=1)
lab1.grid(row=1, column=0, columnspan=2)
cbut0.grid(row=2, column=0)
cbut1.grid(row=2, column=1)
cbut2.grid(row=3, column=0)
cbut3.grid(row=3, column=1)
lab2.grid(row=7, column=0, columnspan=2)
ent1.grid(row=8, column=0, columnspan=2)
but_gen.grid(row=9, column=0)
but_exit.grid(row=9, column=1)


root.mainloop()
