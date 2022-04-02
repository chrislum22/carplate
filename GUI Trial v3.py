# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:23:27 2022

@author:　ジエイコブ先輩
"""

from tkinter import *
from tkinter.ttk import Combobox

def remove_letters(x):
    res = ''.join(filter(lambda i: i.isdigit(), x))
    return res
    
def remove_numbers(x):
    letters = ""
    for char in x:
        if char.isalpha():
            letters += char
    return letters
    

class MyWindow:
    def __init__(self,win):
        self.lbl1=Label(win, text='Input CarPlate')
        self.lbl2=Label(win, text='Checksum Letter')
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=200)
        self.t1=Entry()
        self.t2=Entry()
        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=200)
        self.btn1 = Button(win, text='Checksum')
        self.b1=Button(win, text='Checksum', command=self.checksum)
        self.b1.place(x=100, y=150)
    def checksum(self):
        value = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))
        y = {0:'A',1:'Z',2:'Y',3:'X',4:'U',5:'T',6:'S',7:'R',8:'P',9:'M',10:'L',11:'K',12:'J',13:'H',14:'G',15:'E',16:'D',17:'C',18:'B'}
        atoz = {chr(i): i - 64 for i in range(ord("A"), ord("A") + 26)}
        snp_letters = remove_numbers(self.t1.get()) #letters
        snp_text = remove_letters(self.t1.get()) #numbers
        len_letters=len(snp_letters)
        len_text=len(snp_text)
        if len_letters==1:
            print("1 letter")
            snp_num1 = [4* (ord(snp_letters[0]) - 64)]
        elif len_letters==2:
            print("2 letter")
            snp_num1 = [9*(ord(snp_letters[0]) - 64),4*(ord(snp_letters[1]) - 64)]
        elif len_letters==3:
            print("3 letter")
            snp_num1 = [9*(ord(snp_letters[1]) - 64),4*(ord(snp_letters[2]) - 64)]
        elif len_letters==4:
            print('4 Letters')
            snp_num1 = [9*(ord(snp_letters[1]) - 64),4*(ord(snp_letters[2]) - 64)]
        if len_text==1:
            print("1 number")
            snp_num2 = [ 0, 0, 0, int(snp_text[0])*2]
        elif len_text==2:
            print("2 number")
            snp_num2 = [ 0,0,int(snp_text[0])*3, int(snp_text[1])*2]
        elif len_text==3:
            print("3 number")
            snp_num2 = [ 0,int(snp_text[0])*4, int(snp_text[1])*3, int(snp_text[2])*2]
        elif len_text==4:
            print("4 number")
            snp_num2 = [ int(snp_text[0])*5, int(snp_text[1])*4, int(snp_text[2])*3, int(snp_text[3])*2]

        remainder=sum(snp_num1+snp_num2) % 19
        result=y[remainder]
        self.t2.delete(0, 'end')
        self.t2.insert(END, str(result))
        
window=Tk()
mywin=MyWindow(window)
window.title('CarPlateChecker69')
window.geometry("400x300+10+10")
window.mainloop()