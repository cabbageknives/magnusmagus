import pandas as pd
import tkinter
from tkinter import *
from functools import partial  
from tkinter import filedialog as fd
import re
import os
from pandas import DataFrame
#import openpyxl needed

def exclude(a1, a2, a3):
               
                a3 = e2.get();
                try2 = a1
                try3 = a1
                #try3.set_index(["BugID"], inplace = True)
                
                bs = a3.split()
                i = 0
                print(bs)
                sizemax = len(try2)
                while (i < sizemax):
                    if(int(try2.SrCount[i])< int(e1.get()) and (try2.State[i] == bs[0] or try2.State[i] == bs[1] or try2.State[i] == bs[2])):
                                                                                                                                    huh = try2.BugID[i]
                                                                                                                                    print (huh)
                                                                                                                                    #try3.set_index(["BugID"], inplace = True)
                                                                                                                                    #try3.drop([try2.BugID[i]], inplace = True)
                                                                                                                                    try3.drop([i], inplace = True)
                                                                                                                                              
                            #print (try2.State[i])
                    i = i+1


                length_try3 = len(try3)
                try4 = try3
                export_excel = try3.to_excel (r'C:\Users\mazhakes\Desktop\output\includes_after_script_1.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path

                

def exclude2(try4):
                filename2 = fd.askopenfilename()
                exf = pd.read_excel(filename2)
                po = pd.read_excel(r'C:\Users\mazhakes\Desktop\output\includes_after_script_1.xlsx')
                po1 = po
                sizemax2 = len(po)
                i = 0
                #try4.set_index(["BugID"], inplace = True)
                feature_dict = {}
                while (i < sizemax2):
                    #print(i)
                    searchesa = po.Feature[i]
                    #print(searchesa)
                    search = searchesa.split(",")
                    searchlen = len(search)
                    k = 0
                    #print(search)
                    i = i+1
                    while(k < searchlen):
                            #print()
                            if search[k] in feature_dict:
                                #print("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat")
                                if feature_dict[search[k]] ==1:
                                    print("review")
                                    
                                elif feature_dict[search[k]] == 2:  
                                    #print(po.BugID[i])
                                    po1.drop([i], inplace = True)
                                    
                            else:
                                term1= exf[exf['Feature'].str.match(search[k])]
                                #do the search in exf (then maybe in files), add to dictionary(drop the tuple?)
                                if term1.empty != True:
                                    #print(term1)
                                    filsearch = term1.lookfor
                                    #print("SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                                    #print("to search for:")
                                    #print(filsearch)
                                    print(str(filsearch))

                                    #start of file search
                                    src_dict = r"C:\Users\mazhakes\Desktop\output\configs\search\Config" #Specify base directory
                                    stringToMatch = str(filsearch)

                                    for stuff in os.listdir(src_dict):
                                        files = os.path.join(src_dict, stuff)
                                        for inside in os.listdir(files):
                                            files2 = os.path.join(files,inside)
                                            strng = open(files2)

                                         #We need to open the files
                                            for line in strng.readlines():
                                                        if stringToMatch in line:
                                                                            matchedLine = line
                                                                            print(matchedLine)
                                                                            feature_dict[search[k]]=1
                                                                            break
                                                        else:
                                                            feature_dict[search[k]]=2
                                                            print("not found")
                                                            print(filsearch)
                                                            print("...................................")
                                                                            

                                                                    
                                    





                                    
                                else:
                                    feature_dict[search[k]] = 1
                                #i need a life                                 
                                                     

                    
                                
                                                              
                            k = k+1
    
                                 
                                    
                                






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

eclude2 = partial(exclude2, try4)

b1 = Button(root,text = "Exclude",command = eclude)  

b1.pack(side = BOTTOM)

b2 = Button(root,text = "Exclude From Feature",command = eclude2)  

b2.pack(side = BOTTOM)







