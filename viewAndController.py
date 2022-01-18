import tkinter as tk
import random

remove1='1'
remove2='2'
remove3='3'
remove4='4'

flag1='q'
flag2='w'
flag3='e'
flag4='r'

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
        
        self.removedName=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(self.removedName)
        
        self.tempList[3].set(random_name)
        


    #react qwer (*within 1 second after remove), mark flag symbol for removed student
    # qwer both are flag, so 1 func is enough?
    def flag(self,event):
        print("flag!")

    #initial view
    def firstInterface(self):
        root=tk.Tk()
        root.wm_attributes('-topmost',1)
        root.title('Model select')
        button_1=tk.Button(root,text='Cold Call Assist',command=lambda:[root.destroy(),self.CCinterface()])
        button_1.grid(row=0,column=0)
        button_2=tk.Button(root,text='Input or output file',command=lambda:[root.destroy(),self.fileInterface()])
        button_2.grid(row=1,column=0)
        root.mainloop()
        
    #tkinter window have been closed, now in termial
    def fileInterface(self):
        
        while True:
            command=input('Input or output file: ')
            commandList=command.split()
            if len(commandList)==2:
                if commandList[0]=='input' or commandList[0]=='output':
                    if commandList[0]=='input':
                        print('Input file',commandList[1])
                    else:
                        print('Output file',commandList[1])
                else:
                    print('Invalid command')
            elif len(commandList)==1:
                if commandList[0]=='quit':
                    break
                else:
                    print('Invalid command')

    #cold call view
    def CCinterface(self):
        self.app = tk.Tk()

        tempList=[]
        for i in self.nameList:
            tempName=tk.StringVar()
            tempName.set(i)
            tempList.append(tempName)
        self.tempList=tempList
        
        self.app.wm_attributes('-topmost',1)
        self.app.title('Cold-Call Assist')
        tk.Label(self.app, text='Next students:').pack(side='left')

        theLabel_1 = tk.Label(self.app, textvariable=self.tempList[0])
        theLabel_1.pack(side='left')
        self.app.bind(remove1,self.removeAndAddStudent_1)

        tk.Label(self.app, text=' ').pack(side='left')
        
        theLabel_2 = tk.Label(self.app, textvariable=self.tempList[1])
        theLabel_2.pack(side='left')
        self.app.bind(remove2,self.removeAndAddStudent_2)

        tk.Label(self.app, text=' ').pack(side='left')

        theLabel_3 = tk.Label(self.app, textvariable=self.tempList[2])
        theLabel_3.pack(side='left')
        self.app.bind(remove3,self.removeAndAddStudent_3)

        tk.Label(self.app, text=' ').pack(side='left')

        theLabel_4 = tk.Label(self.app, textvariable=self.tempList[3])
        theLabel_4.pack(side='left')
        self.app.bind(remove4,self.removeAndAddStudent_4)
        
        buttonBack=tk.Button(self.app,text='Back',command=lambda:[self.app.destroy(),self.firstInterface()])
        buttonBack.pack(side='down')
        
        self.app.bind(flag1,self.flag)
        self.app.bind(flag2,self.flag)
        self.app.bind(flag3,self.flag)
        self.app.bind(flag4,self.flag)
        
        self.app.mainloop()



        
