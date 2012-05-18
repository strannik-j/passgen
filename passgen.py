#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  passgen.py
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
from random import randrange

root = Tk(screenName=None, className='PassGen')
frame0 = Frame(root, width=100, height=100)


ent_text0 = StringVar()
ent_text1 = IntVar()


var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

var0.set(1)
var1.set(1)
var2.set(1)
var3.set(0)
ent_text0.set(6)
ent_text1.set('')

pass0 = StringVar()


pa = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
pA = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
p0 = ('0','1','2','3','4','5','6','7','8','9')
px = ('@','#','$','%','^','&','*','!',':',';','_','+','-','.',',','?')


M = []


def main():
	ent_text0 = 5
	return 0


def gen(event):
	M = []
	ch0 = 0
	ch1 = int(ent_text0.get())
	pass0 = ''
	if var0.get() == 1:
		M.extend(pa)
	if var1.get() == 1:
		M.extend(pA)
	if var2.get() == 1:
		M.extend(p0)
	if var3.get() == 1:
		M.extend(px)
	lenM = len(M)
	
	while ch0 < ch1:
		rand0 = randrange(0, lenM, 1)
		pass0 += str(M[rand0])
	
		ch0 += 1
	ent_text1.set(pass0)
	M = []
	return 0
	

def _exit(event):
	sys.exit()
	

but_gen = Button(frame0, text="Generate", width=7)
but_gen.bind("<Button-1>", gen)
but_exit = Button(frame0, text='Exit', width=4)
but_exit.bind("<Button-1>", _exit)


cbut0 = Checkbutton(frame0,text="abc", variable=var0,onvalue=1,offvalue=0)
cbut1 = Checkbutton(frame0,text="ABC", variable=var1,onvalue=1,offvalue=0)
cbut2 = Checkbutton(frame0,text="012", variable=var2,onvalue=1,offvalue=0)
cbut3 = Checkbutton(frame0,text="!@#", variable=var3,onvalue=1,offvalue=0)


ent0 = Entry(frame0, width=5, bd=3, textvariable=ent_text0)
ent1 = Entry(frame0, width=22, bd=3, textvariable=ent_text1)


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

if __name__ == '__main__':
	main()

root.mainloop()
