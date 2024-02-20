# importing tkinter module
import pickle
from tkinter import *
from tkinter import messagebox
filename = 'betalinger.pk'
class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        ##todo: Lav en messagebox, hvor man skriver sit brugernavn ind først

        Label(self.payWindow,
              text="Indbetal").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()
        ##todo: Gem de penge der er indtastet i betalinger.pk
    def safe(self):
        try:
            outfile = open(filename, 'wb')  # Open file in write binary mode
            pickle.dump(fodboldtur, outfile)  # Serialize the dictionary to the file
            outfile.close(self.payWindow)  # Close the file
            print("Pengene er gemt!")  # Print a message indicating program exit
        except:
            messagebox.showerror(parrent=self.payWindow, title="Lortet virker ikke",message="Prøv igen.\ndu har gjort noget forkert!")
            return
        ##todo: Gør det ved hjælp af en "gem og gå til main knap"
        self.button = Button(self.payWindow, text="MAIN", command=self.safe)
        self.button.pack()

    def addMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
    ##Todo: Gør så man også kan trække penge fra hvis man taster det forkerte beløb ind
