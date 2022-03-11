import tkinter as tk
import requests
import get_schedule
from bs4 import BeautifulSoup

root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 500)
canvas1.pack()

label1 = tk.Label(root, text='Enter team name')
label1.config(font=('Arial', 25))
canvas1.create_window(400, 100, window=label1)

entry1 = tk.Entry (root)
canvas1.create_window(400, 150, window=entry1) 

canvas2 = tk.Canvas(root, width = 200, height = 200)
canvas2.pack()

def run_script(): 
    global x1
    x1 = str(entry1.get())
    site = get_schedule.get_id(x1)
    l = []
    r = requests.get(site)
    c = r.content

    s = BeautifulSoup(c,"html.parser")
    a = s.findAll("div",{"id":"teamhome-next-wrap"})
    print(a)
    try:
        for i in a:
            d ={}
            d["Date and Time"] = i.find("div",{"class":"sptime"}).text.replace(u'\xa0', u' ')
            d["Team"] = i.find("span",{"class":"team2name"}).text
            l.append(d)
        game = l[0]["Date and Time"]
        team = l[0]["Team"]
        s =  'Next Game is \n' + game +'\n'
        ss= 'Opponent: \n'+ team

        label = tk.Label(root, text= s,font=('Arial', 20))
        #label.pack()
        canvas2.create_window(-100, 40, window=label) 
        label2 = tk.Label(root, text=ss ,font=('Arial', 20))
        canvas2.create_window(250,25, window=label2) 

        #label2.pack()


        
    except Exception:
        print("No Schedule available")

def Reset():
    canvas2.delete("all")
           
           




button1 = tk.Button (root, text='Check schedule ',command=run_script, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 220, window=button1)

button2 = tk.Button (root, text='Clear ',command=Reset, bg='lightskyblue2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 260, window=button2)

button3 = tk.Button (root, text='Exit', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400,300 , window=button3)
 
root.mainloop()
