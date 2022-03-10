import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import get_schedule
root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 800, height = 500)
canvas1.pack()

label1 = tk.Label(root, text='Next game is ')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)


def run_script(): 
    x =  get_schedule.get_schedule()
    label = tk.Label(root, text= str(x),font=('Arial', 30, 'bold'))
    #entry1.insert(0,label)
    #canvas1.create_window(150, 20, window=label)
    #this creates a new label to the GUI
    label.pack(pady=5) 

            
button1 = tk.Button (root, text=' Run Script ',command=run_script, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 220, window=button1)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400,300 , window=button3)
 
root.mainloop()