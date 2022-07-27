import tkinter as tk
from tkinter import ttk
import workingCode

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("300x170")
        self.master.title("Prune The Links!")

        self.create_widgets()

    def create_widgets(self):
        self.var = tk.StringVar()

        self.label_hello = ttk.Label(self)
        self.label_hello.configure(text='Please Input Links Copied From Xenu')
        self.label_hello.pack()

        self.label_hello2 = ttk.Label(self)
        self.label_hello2.configure(text='(Must CTRL + V to paste)')
        self.label_hello2.pack()

        self.name = tk.StringVar()
        self.entry_name = ttk.Entry(self)
        self.entry_name.configure(textvariable = self.name)
        self.entry_name.pack()

        self.label_hello1 = ttk.Label(self)
        self.label_hello1.configure(text='Please Input Pruning String')
        self.label_hello1.pack()

        self.name1 = tk.StringVar()
        self.entry_name1 = ttk.Entry(self)
        self.entry_name1.configure(textvariable = self.name1)
        self.entry_name1.pack()

        self.button_hello = ttk.Button(self)
        self.button_hello.configure(text="Return Links With Phrase")
        self.button_hello.configure(command = self.say_Hello) 
        self.button_hello.pack()

        self.button_hello1 = ttk.Button(self)
        self.button_hello1.configure(text="Return Links Without Phrase")
        self.button_hello1.configure(command = self.say_Hello1) 
        self.button_hello1.pack()

        self.label_name=ttk.Label(self)
        self.label_name.configure(text = 'Updates')
        self.label_name.pack()

    def say_Hello(self):
        workingCode.populateTxtFile(self.name.get(),"links.txt")
        workingCode.pruneStringWith(self.name1.get())
        self.label_name.configure(text="Links With Pruned Phrase in prunedwith.txt!")
    
    def say_Hello1(self):
        workingCode.populateTxtFile(self.name.get(),"links.txt")
        workingCode.pruneString(self.name1.get())
        self.label_name.configure(text="Links Without Pruned Phrase in prunedwithout.txt!")



def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()