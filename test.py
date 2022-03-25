import tkinter as Tkinter
import get_schedule
coordinates = [[25, 40], [410, 40], [650, 40],
               [35, 180], [200, 180], [410, 180], [655, 180]]
root= Tkinter.Tk()
  
canvas1 = Tkinter.Canvas(root, width = 800, height = 500)
canvas1.pack()
entry1 = Tkinter.Entry (root)
canvas1.create_window(400, 150, window=entry1) 

canvas2 = Tkinter.Canvas(root, width = 200, height = 200)
canvas2.pack()
def run_script(): 
    global x1
    x1 = str(entry1.get())
    site = get_schedule.get_id(x1)
    l = []
    #try:
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
    for h in l:
        print(h)
message = run_script()
  
labels = []
interval = 0

root = Tkinter.Tk()
root.geometry("750x210")

for (x,y), msg in zip(coordinates, message):
    lab = Tkinter.Label(root, text=msg)
    labels.append(lab)
    root.after(interval, lambda a=x,b=y,l=lab:l.place(x=a, y=b))
    interval += 500

root.mainloop()