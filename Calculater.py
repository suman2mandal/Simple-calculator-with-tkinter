import tkinter as tk

def Insert(Entry,data):
    Entry.insert(0,data)
    print(data)

root = tk.Tk()


Top = tk.Frame(bg="black")
Entry = tk.Entry(Top,width=50,bg="black",fg="white")
Entry.grid(row=0,column=0)
Top.pack(side="top")



MidleLeft = tk.Frame(bg="black")

#First Row
Button1 = tk.Button(MidleLeft,text="1",width=6,bg="black",fg="white")
Button1.grid(row=0,column=0)
Button1.bind("<Button-1>",Insert(Entry,1))

Button2 = tk.Button(MidleLeft,text="2",width=6,bg="black",fg="white")
Button2.grid(row=0,column=1)
Button1.bind("<Button-1>",Insert(Entry,2))

Button3 = tk.Button(MidleLeft,text="3",width=6,bg="black",fg="white")
Button3.grid(row=0,column=2)
Button1.bind("<Button-1>",Insert(Entry,3))


#Second Row Left side
Button4 = tk.Button(MidleLeft,text="4",width=6,bg="black",fg="white")
Button4.grid(row=1,column=0)
Button1.bind("<Button-1>",Insert(Entry,4))

Button5 = tk.Button(MidleLeft,text="5",width=6,bg="black",fg="white")
Button5.grid(row=1,column=1)
Button1.bind("<Button-1>",Insert(Entry,5))

Button6 = tk.Button(MidleLeft,text="6",width=6,bg="black",fg="white")
Button6.grid(row=1,column=2)
Button1.bind("<Button-1>",Insert(Entry,6))


#Third Row
Button7 = tk.Button(MidleLeft,text="7",width=6,bg="black",fg="white")
Button7.grid(row=2,column=0)
Button1.bind("<Button-1>",Insert(Entry,7))

Button8 = tk.Button(MidleLeft,text="8",width=6,bg="black",fg="white")
Button8.grid(row=2,column=1)
Button1.bind("<Button-1>",Insert(Entry,8))

Button9 = tk.Button(MidleLeft,text="9",width=6,bg="black",fg="white")
Button9.grid(row=2,column=2)
Button1.bind("<Button-1>",Insert(Entry,9))


MidleLeft.pack(side="left")




#Second Row Right Side
MidleRight = tk.Frame(bg="black")

ButtonPlus = tk.Button(MidleRight,text="+",width=8,bg="black",fg="White")
ButtonPlus.grid(row=0,column=0,sticky='W')

ButtonPlus = tk.Button(MidleRight,text="-",width=8,bg="black",fg="White")
ButtonPlus.grid(row=0,column=1,sticky='W')

ButtonPlus = tk.Button(MidleRight,text="*",width=8,bg="black",fg="White")
ButtonPlus.grid(row=1,column=0,sticky='W')

ButtonPlus = tk.Button(MidleRight,text="/",width=8,bg="black",fg="White")
ButtonPlus.grid(row=1,column=1,sticky='W')

MidleRight.pack(side="right")



root.mainloop()