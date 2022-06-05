import random
import tkinter as tk
from tkinter import *

def crosschecker(n):
    return {
        1:'STONE',
        2:'PAPER',
        3:'SCISSOR',
        }[n]

score=0
val=0
v=""
def win():
    global score
    score+=1
    
comp=0
def lose():
    global comp
    comp+=1

def final():
    if score+comp>3:
        label2=tk.Label(frame,text="your score: "+str(score),bg="yellow")
        label2.pack()
        root.quit
    
list1=[1,2,3]

def stones():
    select='STONE'
    shuff(select)

def papers():
    select='PAPER'
    shuff(select)

def scissors():
    select='SCISSOR'
    shuff(select)

def shuff(sel):        
    num=random.choice(list1)
    v=crosschecker(num)
    label=tk.Label(frame,text="Random Choice Value: "+v+" & You Selected: "+sel,bg="grey")
    label.pack()
    if v==sel:
        label1=tk.Label(frame,text=":YOU GAIN: ",bg="light blue")
        label1.pack()
        win()
    else: 
        label1=tk.Label(frame,text="you lose",bg="red")
        label1.pack()
        lose()
    final()


root=tk.Tk()

root.title('ROCK PAPER SCISSOR')

canvas = tk.Canvas(root,height=500,width=800,bg="blue")
canvas.pack()

frame =tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

button1=tk.Button(frame,text="STONE",padx=1,pady=1,fg="black",bg="yellow", command=stones)
button1.pack()

button2=tk.Button(frame,text="PAPER",fg="black",bg="white",command=papers)
button2.pack()

button3=tk.Button(frame,text="SCISSOR",fg="black",bg="red",command=scissors)
button3.pack()

button3=tk.Button(frame,text="exit",fg="white",bg="black",command=root.quit)
button3.pack()
        
root.mainloop()
    
