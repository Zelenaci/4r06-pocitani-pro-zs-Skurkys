import tkinter as tk
from random import randint
from tkinter import LabelFrame, Radiobutton, Entry, Checkbutton, Label


class Application(tk.Tk):
    name = "PRIKLADY"
    
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.operaceFrame = LabelFrame(self, text="Co chceš procvičit?", padx=5, pady=5)
        self.operaceFrame.pack()
        self.bbn = tk.Checkbutton(self.operaceFrame, text="Sčítání", command=self.plus)
        self.bbn.pack(anchor=tk.W)
        self.bbn = tk.Checkbutton(self.operaceFrame, text="Odčítání", command=self.minus)
        self.bbn.pack(anchor=tk.W)
        self.bbn = tk.Checkbutton(self.operaceFrame, text="Násobení", command=self.krat)
        self.bbn.pack(anchor=tk.W)
        self.bbn = tk.Checkbutton(self.operaceFrame, text="Dělení", command=self.deleno)
        self.bbn.pack(anchor=tk.W)
        
        
        self.lblfr = LabelFrame(self, text='Příklad')
        self.lblfr.pack()
        
        self.entcisloa = Label(self.lblfr,text=None, width=5)
        self.entcisloa.grid(row=1, column=1)
        
        self.entznam = Label(self.lblfr,text=None, width=5)
        self.entznam.grid(row=1, column=2)
        
        self.entcislob = Label(self.lblfr,text=None, width=5)
        self.entcislob.grid(row=1, column=3)
        
        self.prkButton = tk.Button(self, text='Priklad', command=self.priklad)
        self.prkButton.pack()
        
        self.kkn = tk.Button(self, text='Vypočítej to!', command=self.vypocet)
        self.kkn.pack()
        
        self.btn = tk.Button(self, text='Quit', command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()
        


    
    def plus(self):
        self.x = randint(1,99)
        self.y = randint(0,100 - self.x)
        self.vysl = self.x + self.y
    
    
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0, self.x)
        self.vysl = self.x - self.y
        
    def krat(self):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.vysl = self.x * self.y
        
        
    def deleno(self):
        self.vysl = randint(1, 9)
        self.y = randint(1, 9)
        self.x = self.vysl * self.y
        
    def vypocet(self):
        operace = (self.plus, self.minus, self.krat, self.deleno)
        nahoda = randint(0, 3)
        funkce = operace[nahoda]
        funkce()
        print()
        print(self.x, funkce.__name__, self.y, '=', self.vysl)
        
    def priklad(self):
        self.entcisloa.get(self.x)
    
app = Application()
app.mainloop()
