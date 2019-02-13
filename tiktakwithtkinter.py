from tkinter import *
root = Tk()
x= 1

def iswinner(i):
    if ((b1['text'] == i and b2['text']==i and b3['text']==i) or
    (b4['text']==i and b5['text']==i and b6['text']==i) or
    (b7['text']==i and b8['text']==i and b9['text']==i) or
    (b1['text'] ==i and b5['text']==i and b9['text']==i)or
    (b3['text']==i and b5['text']==i and b7['text']==i)):
        return True
def show(btn):
    global x
    x+=1
    if btn['text']==" ":
        if x%2==0:
            btn['text']="0"
            if iswinner("0"):
                print(f"0 winner")
                root.destroy()
        else:
            btn['text']="X"
            if iswinner("X"):
                print(f"X winner")
                root.destroy()
    
# root.geometry("500x400")
root.resizable(0,0)
root.title("t")
#get value from the entry
b1 = Button(root, text=" ",width = 5,command = lambda : show(b1),font= ("Arial",15))
b1.grid(row=0,column=0)

b2 = Button(root, text=" ",width = 5,command = lambda : show(b2),font= ("Arial",15))
b2.grid(row=0,column=1)

b3 = Button(root, text=" ",width = 5,command = lambda : show(b3),font= ("Arial",15))
b3.grid(row=0,column=2)

b4 = Button(root, text=" ",width = 5,command = lambda : show(b4),font= ("Arial",15))
b4.grid(row=1,column=0)

b5 = Button(root, text=" ",width = 5,command = lambda : show(b5),font= ("Arial",15))
b5.grid(row=1,column=1)

b6 = Button(root, text=" ",width = 5,command = lambda : show(b6),font= ("Arial",15))
b6.grid(row=1,column=2)

b7 = Button(root, text=" ",width = 5,command = lambda : show(b7),font= ("Arial",15))
b7.grid(row=2,column=0)

b8 = Button(root, text=" ",width = 5,command = lambda : show(b8),font= ("Arial",15))
b8.grid(row=2,column=1)

b9 = Button(root, text=" ",width = 5,command = lambda : show(b9),font= ("Arial",15))
b9.grid(row=2,column=2)

root.mainloop()