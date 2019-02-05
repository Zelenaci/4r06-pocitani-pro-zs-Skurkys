#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:03:01 2019

@author: sku35268
"""

import tkinter as tk
from random import randint, sample
from tkinter import LabelFrame, Radiobutton, Entry, Label


class Application(tk.Tk):
    name = "PRIKLADY"
    
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.operaceFrame = LabelFrame(self, text="Co chceš procvičit?", padx=5, pady=5)
        self.operaceFrame.pack()
        self.bbn = tk.Radiobutton(self.operaceFrame, text="Sčítání",value = 0,  command=self.plus)
        self.bbn.pack(anchor=tk.W)
        self.bbm = tk.Radiobutton(self.operaceFrame, text="Odčítání",value = 1, command=self.minus)
        self.bbm.pack(anchor=tk.W)
        self.bmn = tk.Radiobutton(self.operaceFrame, text="Násobení",value = 2, command=self.krat)
        self.bmn.pack(anchor=tk.W)
        self.bnn = tk.Radiobutton(self.operaceFrame, text="Dělení",value = 3,command=self.deleno)
        self.bnn.pack(anchor=tk.W)
        
        
        self.lblfr = LabelFrame(self, text='Příklad')
        self.lblfr.pack()
        
        self.entcisloa = Label(self.lblfr,text=None, width=5)
        self.entcisloa.grid(row=1, column=1)
        
        self.entznam = Label(self.lblfr,text=None, width=5)
        self.entznam.grid(row=1, column=2)
        
        self.entcislob = Label(self.lblfr,text=None, width=5)
        self.entcislob.grid(row=1, column=3)
        
        self.pol = Entry(self, width = 4)
        self.pol.pack()
        
        
        self.kkn = tk.Button(self, text='Vypočítej to!', command=self.vypocet)
        self.kkn.pack()
        
        self.btn = tk.Button(self, text='Quit', command=self.quit)
        self.btn.pack()

   
    
    def quit(self, event=None):
        super().quit()
        

    global operaces
    operaces=list()
    
    def plus(self):
        self.x = randint(1,99)
        self.y = randint(0,100 - self.x)
        self.vysl = self.x + self.y
        operaces.append(self.plus)
    
    
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0, self.x)
        self.vysl = self.x - self.y
        operaces.append(self.minus)
        
    def krat(self):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.vysl = self.x * self.y
        operaces.append(self.krat)
        
        
    def deleno(self):
        self.vysl = randint(1, 9)
        self.y = randint(1, 9)
        self.x = self.vysl * self.y
        operaces.append(self.deleno)
        
    def vypocet(self):
        operace = sample(operaces, 1)
        funkce = operace
        print(operace)
        funkce()
        print()
        print(self.x, funkce.__name__, self.y, '=', self.vysl)
        
    def priklad(self):
        self.entcisloa.get(self.x)
        
    
    
    
app = Application()
app.mainloop()