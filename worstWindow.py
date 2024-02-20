# importing tkinter module
from tkinter import *
from PIL import ImageTk,Image

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("1400x900")

        Label(self.worstWindow, text="De værste betalere").pack()

        ##todo: Lav et if statement der bestemmer om worst window skal åbne podie123(1) eller podie123(2)
        #todone: Få importeret et billede af et podie
        img = ImageTk.PhotoImage(Image.open("assets/podie123/PODIE123.png"))
        panel = Label(self.worstWindow, image=img)
        panel.image = img
        panel.pack(side="bottom", fill="both", expand="yes")
        ##Todo: Print navnene ud på de tre eller fire personer som har betalt mindst

        ##Todo: Gør så hver af navnene bliver placeret korrekt på siden så det ligner de er på hver deres podie
