# -*- coding: utf-8 -*-
"""odev3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fl3fmvmb2HL5CwhKlh0bkJRvA4d-9Bek
"""

students={}
notes=[]

for i in range(5):
    name = input (str(i+1)+". Öğrencinin adını giriniz\n")
    midterm = float (input (str(i+1) + ". Öğrencinin vize notunu giriniz\n"))
    project = float (input (str(i+1) + ". Öğrencinin proje notunu giriniz\n"))
    final   = float (input (str(i+1) + ". Öğrencinin final notunu giriniz\n"))
    if (midterm and project and final < 0) or (midterm and project and final>100):
        print ("hatalı giriş") 
    else:
        passingGrade = midterm*(0.3)+project*(0.3)+final*(0.4)
        students[name]=midterm,project,final,passingGrade        
        notes.append(passingGrade)
notes.sort(reverse=True)
print(students)
print (notes)