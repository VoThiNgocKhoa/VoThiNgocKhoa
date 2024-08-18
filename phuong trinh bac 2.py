# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:25:55 2024

@author: 84372
"""

import math 
a=float(input("nhap a :"))
b=float(input("nhap b :"))
c=float(input("nhap c :"))
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh co vo so nghiem ")
        else :
           print("phuong trinh vo nghiem ")
    else:
        x=-c/b
        print("phuong trinh co nghiem duy nhat ")

else:
    delta=b**2-4*a*c
    if delta>0:
        x1 =(-b+math.sqrt (delta))/(2*a)
        x2 =(-b-math.sqrt (delta))/(2*a)
        print(x1,x2 )
    elif delta==0:
        x=-b/(2*a )
        print("nghiem kep " ,x )
    else:
        print("phương trinh vo nghiem ")5