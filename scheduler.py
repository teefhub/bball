import tkinter as tk
import requests
import get_schedule
from bs4 import BeautifulSoup
import re

root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 400)
canvas1.pack()

label1 = tk.Label(root, text='Enter team name')
label1.config(font=('Arial', 25))
canvas1.create_window(400, 50, window=label1)

entry1 = tk.Entry (root)
canvas1.create_window(400, 100, window=entry1) 

canvas2 = tk.Canvas(root, width = 200, height = 200)
canvas2.pack()


def run_script(): 
    global x1
    x1 = str(entry1.get())
    site = get_schedule.get_id(x1)
    l = []
    try:
        for i in site:
            r = requests.get(i)
            c = r.content
            s = BeautifulSoup(c,"html.parser")
            a = s.find_all("div",{"id":"teamhome-next-wrap"})
            for j in a:
                d ={}
                d["Date and Time"] = j.find("div",{"class":"sptime"}).text.replace(u'\xa0', u' ')
                d["Team"] = j.find("span",{"class": re.compile('(team2name|team1name)')}).text
                l.append(d)
        
        result = l
        lbl.config(text=result)

    except AttributeError:
        print("No schedule available")
lbl = tk.Label(
    root,
#    bg='#5f734c', 
    font=(200)
    )
lbl.pack(expand=True)


def Reset():
    canvas2.delete("all")
    
button1 = tk.Button (root, text='Check schedule ',command=run_script, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 150, window=button1)

button2 = tk.Button (root, text='Clear ',command=Reset, bg='lightskyblue2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 200, window=button2)

button3 = tk.Button (root, text='Exit', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400,250 , window=button3)
 
root.mainloop()
