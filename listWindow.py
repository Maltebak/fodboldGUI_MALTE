# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over Brugere og deres indbetalinger").pack()

        ##todo: print liste over folk og values
        for item in self.master.fodboldtur.items():
            print(item)
        self.leftFrame = Frame(self.listWindow, borderwidth=2, relief=GROOVE)
        self.leftFrame.pack(side=LEFT, fill=BOTH, expand=False)  # Changed expand to False
        for item in self.master.fodboldtur:
            Label(self.leftFrame, text=item).pack(side=TOP, anchor='w', padx=(0, 15))  # Align labels to the left
        ##todo: Lave en button der går tilbage til MENU og lukker fanen

