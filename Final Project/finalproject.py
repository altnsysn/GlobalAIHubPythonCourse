# -*- coding: utf-8 -*-
"""finalProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jh88Z1Y_eJ9tDv-k4fzZqmiFDuoXueFd
"""

appIsStarted = True
def sorular():
    ques={1:["Soru 1","a"],2:["Soru 2","A"],3:["Soru 3","ab"],4:["Soru 4","Ab"],5:["Soru 5","a"],6:["Soru 6","a"],7:["Soru 7","a"],8:["Soru 8","a"],
      9:["Soru 9","a"],10:["Soru 10","a"]}
    point = 0
    for i in range(len(ques.keys())):
        cevap = input(ques[i+1][0])
        print ("\n")
        if cevap == ques[i+1][1]:
            point += 10
            print("Tebrikler doğru cevap..\n Mevcut puannız = " + str(point)+"\n")
        else:
          print("Yanlış cevap verdiniz..\n Mevcut puanınız= " + str(point)+"\n")    
    if point >= 50:
        print("tebrikler kazandınız puanınız = "+ str(point)+"\n")
        point = 0
    else:   
        print ("kaybettiniz puanıznız = "+ str(point)+"\n")
        point = 0
while appIsStarted == True:
    a = int(input ("1.Play\n2.Exit"))
    if a == 1:
        sorular()
    elif a == 2:
        appIsStarted = False
    else:
        print("Hatalı giriş\n")