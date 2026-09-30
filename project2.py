from tkinter import*
top=Tk()
entry=Entry(top)
entry.pack
Lb1=Listbox(top)
Lb1.insert(1,"python")
Lb1.insert(2,"java")
Lb1.insert(3,"c++")
Lb1.pack()
def show_item():
    selected=Lb1.curselection()
    if selected:
        item=Lb1.get(selected[0])
        entry.delete(0,"end")
        entry.insert(0,item)
        print(item)
button1=Button(top,text="نمايش انتخاب",command=show_item)
button1.pack()
button2=Button(top,text="دکمه2",command=show_item)
button2.pack()
button3=Button(top,text="دکمه3",command=show_item)
button3.pack()
top.mainloop
