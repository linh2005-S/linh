# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:43:02 2024

@author: MUONVELAM
"""

import random
print("Trò chơi kéo búa bao")
nguoichon = input("Nhập lựa chọn: ")
print("nguoichoichon", nguoichon)
maychon=random.choice(["kéo","búa","bao"])
print("maychon: ", maychon)
if nguoichon==maychon:
    print("hòa")
elif (nguoichon=="kéo" and maychon=="bao")or(nguoichon=="búa" and maychon=="kéo"):
    print("thắng")
elif (nguoichon=="bao" and maychon=="kéo")or(nguoichon=="kéo" and maychon=="búa"):
    print("thua")
else:
    print("nhập sai,máy không biết")