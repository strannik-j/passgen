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


def main():
    x = sys.argv[1:]
    t = []
    try:
        for i in x:
            t.append(int(i))
    except:
        print('''Usage: passgen.py [a] [b] [c] [d]
        a: quantity of characters (Default - 8)
        b: usage "abc" (1 - yes, 0 - no; Default - 1)
        c: usage "ABC" (1 - yes, 0 - no; Default - 1)
        d: usage "123" (1 - yes, 0 - no; Default - 1)
        e: usage "!@#" (1 - yes, 0 - no; Default - 0) \
        ''')
        sys.exit()

    if len(t) == 0:
        password = generate()
    elif len(t) == 1:
        password = generate(t[0])
    elif len(t) == 2:
        password = generate(t[0], t[1])
    elif len(t) == 3:
        password = generate(t[0], t[1], t[2])
    elif len(t) == 4:
        password = generate(t[0], t[1], t[2], t[3])
    else:
        password = generate(t[0], t[1], t[2], t[3], t[4])
    print(password)
    return 0


def generate(var_len=8, vpa=1, vpA=1, vp0=1, vpx=0):
    pa = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    pA = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    p0 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    px = ('@', '#', '$', '%', '^', '&', '*',
          '!', ':', ';', '_', '+', '-', '.', ',', '?')
    M = []
    ch0 = 0
    pass0 = ''

    if vpa + vpA + vp0 + vpx == 0:
        print('ERROR: no characters for password')
        sys.exit()


    if vpa == 1:
        M.extend(pa)
    if vpA == 1:
        M.extend(pA)
    if vp0 == 1:
        M.extend(p0)
    if vpx == 1:
        M.extend(px)
    lenM = len(M)

    spa = set(pa)
    spA = set(pA)
    sp0 = set(p0)
    spx = set(px)

    while ch0 <= var_len:
        if ch0 == var_len:

            spass0 = set(pass0)

            if vpa == 1 and var_len > 0:
                if spass0 & spa == set():
                    pass0 = ""
                    ch0 = 0

            if vpA == 1 and var_len > 1:
                if spass0 & spA == set():
                    pass0 = ""
                    ch0 = 0

            if vp0 == 1 and var_len > 2:
                if spass0 & sp0 == set():
                    pass0 = ""
                    ch0 = 0

            if vpx == 1 and var_len > 3:
                if spass0 & spx == set():
                    pass0 = ""
                    ch0 = 0

            if ch0 != 0:
                ch0 = var_len + 1
        if ch0 < var_len:
            rand0 = randrange(0, lenM, 1)
            pass0 += str(M[rand0])
            ch0 += 1

    M = []
    return pass0


def _exit(event):
    sys.exit()


if __name__ == '__main__':
    main()
else:
    print('import module passgen')
