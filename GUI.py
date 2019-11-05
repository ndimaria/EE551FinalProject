import tkinter as tk
import FinalProject as FP
from tkinter import StringVar, IntVar

root = tk.Tk()

text = StringVar()
text.set('old')
status = IntVar()

def change():
    lb.config(text = FP.searchWebsite("AAPL"))

cb = tk.Button(root, text = "OK", command=change)
lb = tk.Label(root, width=50, text="Old Text")
cb.pack()
lb.pack()

root.mainloop()
