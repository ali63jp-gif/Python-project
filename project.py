##from tkinter import*
##top=Tk()
##entry=Entry(top)
##entry.pack()
##top.mainloop()
##print("******")
##from tkinter import*
##top=Tk()
##Lb1=Listbox(top)
##Lb1.insert(1,"python")
##Lb1.insert(2,"java")
##Lb1.insert(3,"c++")
##Lb1.insert(4,"javaScript")
##Lb1.pack()
##top.mainloop()
##print("*****")
##from tkinter import*
##top=Tk()
##button=Button(top,text="دکمه1")
##button.pack()
##button2=Button(top,text="دکمه2")
##button2.pack()
##button3=Button(top,text="دکمه3")
##button3.pack()
##top.mainloop()
##print("*******")
##from tkinter import*
##top=Tk()
##def test():
##    print("دکمه کار کرد")
##button=Button(top,text="کليک کن",command=test)
##button.pack()
##top.mainloop
##
##from tkinter import*
##top=Tk()
##def Show_item():
##    selected=Lb1.curselection()
##    item=Lb1.get(active)
##    print(item)
##entry=Entry(top)
##entry.pack()
##Lb1=Listbox(top)
##Lb1.insert(1,"python")
##Lb1.insert(2,"java")
##Lb1.insert(3,"c++")
##Lb1.insert(4,"javaScript")
##Lb1.pack()
##button=Button(top,text="دکمه1")
##button.pack()
##button2=Button(top,text="دکمه2")
##button2.pack()
##button3=Button(top,text="دکمه3")
##button3.pack()
##top.mainloop()
##print("*******")
##from tkinter import*
##top=Tk()
##Lb1=Listbox(top)
##Lb1.insert(1,"python")
##Lb1.pack()
##def show_item():
##    selected=Lb1.curselection()
##    item=Lb1.get(selected[0])
##    print(item)
##button=Button(top,text="نمايش",command=show_item)
##button.pack()
##top.mainloop()
##print("*******")
##from tkinter import*
##top=Tk()
##Lb1=Listbox(top)
##Lb1.insert(1,"python")
##Lb1.insert(2,"java")
##Lb1.insert(3,"c++")
##Lb1.insert(4,"javaScript")
##Lb1.pack()
##top.mainloop()
##print("*****")
##from tkinter import*
##top=Tk()
##button=Button(top,text="دکمه1")
##button.pack()
##button2=Button(top,text="دکمه2")
##button2.pack()
##button3=Button(top,text="دکمه3")
##button3.pack()
##top.mainloop()
##print("*******")
##from tkinter import*
##top=Tk()
##def test():
##    print("دکمه کار کرد")
##button=Button(top,text="کليک کن",command=test)
##button.pack()
##top.mainloop
##
##from tkinter import*
##top=Tk()
##Lb1=Listbox(top)
##Lb1.insert(1,"python")
##Lb1.insert(2,"java")
##Lb1.insert(3,"c++")
##Lb1.pack()
##def show_python():
##    print(Lb1.get(0))
##def show_java():
##    print(Lb1.get(1))
##def show_cpp():
##    print(Lb1.get(2))    
##button1=Button(top,text="نمايش python",command=show_python)
##button1.pack()
##button2=Button(top,text="نمايش java",command=show_java)
##button2.pack()
##button3=Button(top,text="نمايش c++",command=show_cpp)
##button3.pack()
##top.mainloop
##print("********")
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



