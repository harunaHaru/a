import tkinter as tk 
from openpyxl import load_workbook
import pandas as pd 
import os
from tkinter import messagebox
def finish():
    if windows.winfo_exists():
        button.config(state=tk.DISABLED) # Düğmeyi devre dışı bırak 
        windows.after(100, windows.destroy)

  
windows = tk.Tk()
windows.geometry("950x700")
windows.configure(bg="#FF0003")
windows.title("restrounat")
FirstLabel= tk.Label(windows, text="restronat", bg="#29394D", fg="#5DE2E7", font=("STENCIL",20), width=55, height=5)
FirstLabel.place(x=10, y=10)
     
l_r_label= tk.Label(windows,bg="#BCDFE1", width=125, height=33)
l_r_label.place(x=8, y=180)

left_label=tk.Label(windows,bg="#29394D", width=50, height=30)
left_label.place(x=15, y=200)

right_label=tk.Label(windows,bg="#29394D", width=69, height=23)
right_label.place(x=390, y=250)

bottom_label=tk.Label(windows,bg="#29394D", width=126, height=23)
bottom_label.place(x=10, y=700)

    
button= tk.Button(windows,bg="#29394D",font=("STENCIL",20) , text='finish' , command=finish)
button.place(x=410, y=610)
coffe=['cafe latte', 'cafe mocha', 'cappunico', 'americano', 'water','filtre coffe', 'chefs special', 'sake']
for i in range(len(coffe)):
        
    entry=tk.Entry(windows,bg="#F2FCFC", width=13,  text="0" )
    entry.place(x=270, y=230 + i*50)
    checkbox= tk.Checkbutton(windows,text=coffe[i], width=14, font=("STENCIL",18) )
    checkbox.place(x=30, y=220 + i*50)
for i in range(4):
    for j in range(4):
        button=tk.Button(windows, bg="#29394D", width=2, height=2 )
        button.place(x=760+i*30, y=280+30*j)
            
windows.mainloop()