import pandas as pd
import tkinter
from tkinter import *
from functools import partial  
from tkinter import filedialog as fd



def exclude(a1, a2, a3):
                a3 = e2.get();
                try2 = a1;
                bs = a3.split()
                i = 0
                print(bs)
                sizemax = len(try2)
                while (i < sizemax):
                    if(int(try2.SrCount[i])< int(e1.get()) and (try2.State[i] == bs[0] or try2.State[i] == bs[1] or try2.State[i] == bs[2])):
                                                                                                                        print (try2.BugID[i])
                            #print (try2.State[i])
                    i = i+1
  










#root = tkinter.top()
root = Tk()
root.geometry("400x300")
root.overrideredirect(True)
filename = fd.askopenfilename()

print(filename)
try4 = pd.read_excel(filename)


#ExcludeSR = Label(root, text = "Exclude if below")
#ExcludeSR.pack()
e1 = Entry(root)
e1.pack(side = TOP)
#e1.grid(row=2, column=1, sticky=W)


e2 = Entry(root)  
e2.pack(side = TOP)
#e2.grid(row=3, column=1, sticky=W)






eclude= partial(exclude, try4, e1.get(), e2.get())  

b1 = Button(root,text = "Exclude",command = eclude)  

b1.pack(side = BOTTOM)







