# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:26:59 2024

@author: 84372
"""

a=float(input("nhap canh a: "))
b=float(input("nhap canh b: "))
c=float(input("nhap canh c: "))
if a + b > c and a + c > b and b + c > a:
    print("a,b,c la ba canh cua tam giac ")
    if a**2+b**2==c**2  or a**2+c**2==b**2  or b**2+c**2==a**2:
        print("tam giac vuong ")
    if a==b==c:
        print("tam giac deu ")
    elif a==b or  b==c or c==a:
        print("tam giac can ")
    else:
        print("day la tam giac thuong ")
else:
    print("day khong là tam giac ")
        
   
            
        
    
        

        
          
 
