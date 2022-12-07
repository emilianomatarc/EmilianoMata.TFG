import tkinter as tk
#from tkinter import font
from Controllers.PlanesPruebaController import PlanesPruebaController


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        #self.geometry(str(screen_width) + "x" + str(screen_height))
        self.state('zoomed')
        self.resizable(False, False)
        #print(screen_width)
        #print(screen_height)
        
        PlanesPruebaController(self)
       

if __name__ == '__main__':
    app = Main()
    #print(font.families())
    #print(tuple(range(10)))
    app.mainloop()
