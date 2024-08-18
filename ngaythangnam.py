# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:17:14 2024

@author: 84372
"""

dmy=input("nhap ngay thang nam theo dinh dang  dd/mm/yyyy: ")
day=int(dmy[0:2])
month=int(dmy[3:5])
year=int(dmy[6:])
if month > 0 and month <= 12:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if month == 2:
            if day < 1 or day > 29:
                print("ngay khong hop le ")
            else:
                print("ngay thang nam hop le ")
        else:
            if month in [4, 6, 9, 11]:
                if day < 1 or day > 30:
                    print("ngay khong hop le ")
                else:
                    print("ngay thang nam hop le ")
            else:
                if day < 1 or day > 31:
                    print("ngay khong hop le ")
                else:
                    print("ngay thang nam hop le ")
    else:
        if month == 2:
            if day < 1 or day > 28:
                print("nagy khong hop le ")
            else:
                print("ngay thang nam  hop le ")
        else:
            if month in [4, 6, 9, 11]:
                if day < 1 or day > 30:
                    print("ngay khong hop le ")
                else:
                    print("ngay thang nam hop le ")
            else:
                if day < 1 or day > 31:
                    print("nagy khong hop le ")
                else:
                    print("ngay thang nam  hop le ")
else:
    print("thang khong hop le ")