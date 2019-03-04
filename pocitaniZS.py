import tkinter as tk
from tkinter import Label, Radiobutton, LabelFrame, IntVar, StringVar, Entry, Message
from random import randint

class Application(tk.Tk):
    name = 'Priklady'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth = 5)
        self.bind("<Escape>", self.quit)
        self.lbloper=Label(self, text=u"Operace:", font='Arial 18')
        self.lbloper.pack(anchor='w')

        self.vyber = StringVar()
        self.vyber.set('')
        
        self.tlaplus = Radiobutton(self, text = u'+', variable=self.vyber, value='+' , font='Arial 20', command=self.plus)
        self.tlaplus.pack(anchor='w')
        
        self.tlaminus = Radiobutton(self, text = u'-', variable=self.vyber, value='-', font='Arial 20', command=self.minus)
        self.tlaminus.pack(anchor='w')
        
        self.tlakrat = Radiobutton(self, text = u'*', variable=self.vyber, value='*' , font='Arial 20', command=self.krat)
        self.tlakrat.pack(anchor='w')
        
        self.tladeleno = Radiobutton(self, text = u'/', variable=self.vyber, value='/' , font='Arial 20', command=self.deleno)
        self.tladeleno.pack(anchor='w')
        
        self.lblfr = LabelFrame(self, text='Příklad')
        self.lblfr.pack(anchor='w')
        
        self.inta = IntVar()
        self.inta.set('')
        
        self.entcisloa = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.inta)
        self.entcisloa.grid(row=1, column=1)
        
        self.znammess = Message(self.lblfr, font='Arial 20', textvariable=self.vyber)
        self.znammess.grid(row=1, column=2)
        
        self.intb = IntVar()
        self.intb.set('')
        
        self.entcislob = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.intb)
        self.entcislob.grid(row=1, column=3)
        
        self.rovmess = Message(self.lblfr, text=u'=', font='Arial 20')
        self.rovmess.grid(row=1, column=4)
        
        self.intvysl = StringVar()
        self.intvysl.set('')
        
        self.entcislob = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.intvysl)
        self.entcislob.grid(row=1, column=5)
        
        self.prkButton = tk.Button(self, text='Nový příklad', command=self.priklad)
        self.prkButton.pack(anchor='w')
        
        self.intuzi = StringVar()
        self.intuzi.set('')
        
        self.entvys = Entry(self, text=None, width=5, font='Arial 20', textvariable=self.intuzi)
        self.entvys.pack()
        
        self.vypButton = tk.Button(self, text='Výpočet', command=self.vypocet)
        self.vypButton.pack()
        
        self.zkoButton = tk.Button(self, text='Zkontroluj výsledek', command=self.zkontroluj)
        self.zkoButton.pack()
        
        self.pormess = Message(self, text='', font='Arial 15')
        self.pormess.pack()
        
        self.lblfrstat = LabelFrame(self, text='Statistika', padx=30)
        self.lblfrstat.pack()
        
        self.sprmess = Message(self.lblfrstat, text='Správně:', font='Arial 18',pady=25)
        self.sprmess.grid(row=1,column=1)
        
        self.intspr = IntVar()
        self.intspr.set(0)
        
        self.entvys = Entry(self.lblfrstat, text=None, width=3, font='Arial 20', textvariable=self.intspr)
        self.entvys.grid(row=1,column=2)
        
        self.spamess = Message(self.lblfrstat, text='Špatně:', font='Arial 18',pady=25)
        self.spamess.grid(row=1, column=3)
        
        self.intspa = IntVar()
        self.intspa.set(0)
        
        self.entvys = Entry(self.lblfrstat, text=None, width=3, font='Arial 20', textvariable=self.intspa)
        self.entvys.grid(row=1,column=4)
        
        
        
        
        
    def plus(self):
        self.intvysl.set('')
        self.x = randint(1,99)
        self.y = randint(0,100-self.x)
        self.vysl = self.x + self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
            
    def minus(self):
        self.intvysl.set('')
        self.x = randint(1,99)
        self.y = randint(0,self.x)
        self.vysl = self.x - self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
        
    def krat(self):
        self.intvysl.set('')
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.vysl = self.x * self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
        
    def deleno(self):
        self.intvysl.set('')
        self.vysl = randint(1,9)
        self.y = randint(1,9)
        self.x = self.vysl * self.y
        self.inta.set(self.x)
        self.intb.set(self.y)

    def vypocet(self):
        self.intvysl.set(self.vysl)
        
    def priklad(self):
        priklad = self.vyber.get()
        if priklad == "+":
            self.tlaplus.invoke()
        if priklad == "-":
            self.tlaminus.invoke()
        if priklad == "*":
            self.tlakrat.invoke()
        if priklad == "/":
            self.tladeleno.invoke()
    
    def zkontroluj(self):
        self.intvysl.set(self.vysl)
        vysl = self.intvysl.get()
        uzivatel = self.intuzi.get()
        if vysl == uzivatel:
            self.pormess.configure(text='Správný výsledek')
            spravne = self.intspr.get()
            spravne = spravne + 1
            self.intspr.set(spravne)
            self.prkButton.invoke()
        else:
            self.pormess.configure(text='Špatný výsledek')
            spatne = self.intspa.get()
            spatne = spatne + 1
            self.intspa.set(spatne)
            self.prkButton.invoke()

    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()