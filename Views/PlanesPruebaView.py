import tkinter as tk
from tkinter import ttk
from tkinter import Entry


class PlanesPruebaView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        parent.title('TestingBotCV - Planes de Prueba')

        ttk.Style().configure("My.TFrame", background="blue")
        self.config(style="My.TFrame")

        #self.label=ttk.Label(self, text='Planes de Prueba', font=('Consolas', 25), justify='center', background="red")
        #self.label.place(x=100, y=100)
        
        #buttons=PlanesPruebaSelectAndSearch(self)
        #buttons.grid(row=1,column=0, rowspan=8, columnspan=6, sticky=tk.NSEW)
#
#        self.upd=PlanesPruebaUpdate(self)
#        self.upd.grid(row=1, column=7, rowspan=5,  columnspan=3, sticky=tl.NSEW)
#
        #self.form=PlanesPruebaForm(self)
        #self.form.grid(row=6, column=7, rowspan=5,  columnspan=3)
        #
        #self.exec=PlanesPruebaExec(self)
        #self.exec.grid(row=9)




class PlanesPruebaSelectAndSearch(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label=ttk.Label(self, text='SELECTANDSEARCH:')
        self.label.grid(row=0, column=0, sticky="NESW")


class PlanesPruebaUpdate(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label=ttk.Label(self, text='UPDATE:')
        self.label.grid(row=0, column=0, sticky="NESW")


class PlanesPruebaForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label=ttk.Label(self, text='FORM:')
        self.label.grid(row=0, column=0, sticky="NESW")


class PlanesPruebaExec(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label=ttk.Label(self, text='EXEC:')
        self.label.grid(row=0, column=0, sticky="NESW")
