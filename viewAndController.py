import tkinter as tk
import random
import time

remove1='1'
remove2='2'
remove3='3'
remove4='4'

flag1='q'
flag2='w'
flag3='e'
flag4='r'

selected_student = '0'
time_since_selected = time.time()

class UserInterface(object):

    def __init__(self, nameList,restList):
        self.nameList=nameList
        self.restList=restList
        self.fileMode=False
        self.removedName=''
        
    def random_select(self):
        #need ramdom algorithm here
        #need insert the removed name back to restList
        return random.choice(self.restList)

    def removeAndAddStudent_1(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList

        global selected_student
        selected_student = 'q'
        global time_since_selected
        time_since_selected = time.time()
        
        self.removedName=self.nameList[0]
        self.nameList[0]=self.nameList[1]
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(self.removedName)
        
        self.tempList[0].set(self.nameList[0])
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)
        
        

    def removeAndAddStudent_2(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList

        global selected_student
        selected_student = 'w'
        global time_since_selected
        time_since_selected = time.time()

        self.removedName=self.nameList[1]
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(self.removedName)
        
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)
        
        

    def removeAndAddStudent_3(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList

        global selected_student
        selected_student = 'e'
        global time_since_selected
        time_since_selected = time.time()

        self.removedName=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(self.removedName)
        
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)
        
       
       
        

    def removeAndAddStudent_4(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList

        global selected_student
        selected_student = 'r'
        global time_since_selected
        time_since_selected = time.time()
        
        self.removedName=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(self.removedName)
        
        self.tempList[3].set(random_name)

    def flag(self,event):
        # check flag matches removed student and occurred within one second
        match_flag = (event.char == selected_student)
        time_difference = time.time() - time_since_selected
        if time_difference <= 1 and match_flag:
            print("flag:",self.removedName)
        
    def inputFile(self,entry):
        print('Input file:',entry.get())
        
    def outputFile(self,entry):
        print('Output file:',entry.get())

    #initial view
    def firstInterface(self):
        root=tk.Tk()
        root.geometry('+0+0')
        root.wm_attributes('-topmost',1)
        root.title('Model select')
        button_1=tk.Button(root,text='Cold Call Assist',command=lambda:[root.destroy(),self.CCinterface()])
        button_1.grid(row=0,column=0)
        button_2=tk.Button(root,text='Input or output file',command=lambda:[root.destroy(),self.fileInterface()])
        button_2.grid(row=1,column=0)
        root.mainloop()
        
    #tkinter window have been closed, now in termial
    def fileInterface(self):
        root=tk.Tk()
        root.geometry('+0+0')
        root.wm_attributes('-topmost',1)
        root.title('File operation')
        entry = tk.Entry(root, bd =5)
        
        entry.grid(row=0,column=1)
        button_1=tk.Button(root,text='Input',command=lambda:self.inputFile(entry))
        button_1.grid(row=1,column=0)
        button_2=tk.Button(root,text='Output',command=lambda:self.outputFile(entry))
        button_2.grid(row=1,column=2)
        button_3=tk.Button(root,text='Back',command=lambda:[root.destroy(),self.firstInterface()])
        button_3.grid(row=2,column=1)
        root.mainloop()
        

    #cold call view
    def CCinterface(self):
        self.app = tk.Tk()
        self.app.geometry('+0+0')
        tempList=[]
        for i in self.nameList:
            tempName=tk.StringVar()
            tempName.set(i)
            tempList.append(tempName)
        self.tempList=tempList
        
        self.app.wm_attributes('-topmost',1)
        self.app.title('Cold-Call Assist')
        tk.Label(self.app, text='Next students:').grid(row=0,column=0)

        theLabel_1 = tk.Label(self.app, textvariable=self.tempList[0])
        theLabel_1.grid(row=0,column=1)
        self.app.bind(remove1,self.removeAndAddStudent_1)

        tk.Label(self.app, text=' ').grid(row=0,column=2)
        
        theLabel_2 = tk.Label(self.app, textvariable=self.tempList[1])
        theLabel_2.grid(row=0,column=3)
        self.app.bind(remove2,self.removeAndAddStudent_2)

        tk.Label(self.app, text=' ').grid(row=0,column=4)

        theLabel_3 = tk.Label(self.app, textvariable=self.tempList[2])
        theLabel_3.grid(row=0,column=5)
        self.app.bind(remove3,self.removeAndAddStudent_3)

        tk.Label(self.app, text=' ').grid(row=0,column=6)

        theLabel_4 = tk.Label(self.app, textvariable=self.tempList[3])
        theLabel_4.grid(row=0,column=7)
        self.app.bind(remove4,self.removeAndAddStudent_4)
    
        
        buttonBack=tk.Button(self.app,text='Back',command=lambda:[self.app.destroy(),self.firstInterface()])
        buttonBack.grid(row=1,sticky='w')
        
        self.app.bind(flag1,self.flag)
        self.app.bind(flag2,self.flag)
        self.app.bind(flag3,self.flag)
        self.app.bind(flag4,self.flag)
        
        self.app.mainloop()

