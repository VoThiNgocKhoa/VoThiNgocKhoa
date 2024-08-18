# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:45:22 2024

@author: 84372
"""
GPA = float(input("nhap diem trung binh:"))
if GPA < 3.5:
    print("hoc luc kem")
elif 3.5 <= GPA < 5.0:
    print("hoc luc yeu")
elif 5.0 <= GPA < 7.0:
    print("hoc luc trung binh")
elif 7.0 <= GPA < 8.0:
    print("hoc luc kha")
elif 8.0 <= GPA < 9.0:
    print("hoc luc trung binh") 
else:
    print("diem khong xac dinh")
    
    
    
