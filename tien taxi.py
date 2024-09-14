# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:47:02 2024

@author: 84372
"""
duong=float(input("nhap quang duong di: "))
if duong==1:
    x=20
    print("tien taxi:" ,x )
elif duong>1  and duong<=3:
    x=duong*13
    print("tien taxi ",x )
elif duong>=4 and  duong<=8:
    x=3*13 +(duong-3  )*12
    print ("tien taxi ",x )
else:
    x=duong*10
    if x>100:
        x=x* 0,92 
        print ("tien taxi ",x )
    else:
        print ("tien taxi ",x )
