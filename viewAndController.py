import tkinter as tk
import random


class UserInterface(object):

    def __init__(self, nameList,restList):
        self.app = tk.Tk()
        self.nameList=nameList
        self.restList=restList
        #self.fileMode=False
        tempList=[]
        for i in nameList:
            tempName=tk.StringVar()
            tempName.set(i)
            tempList.append(tempName)
        self.tempList=tempList
        
    def random_select(self):
        #need ramdom algorithm here
        #need insert the removed name back to restList
        return random.choice(self.restList)

    def removeAndAddStudent_1(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList
        print('place 1')
        removedName=self.nameList[0]
        self.nameList[0]=self.nameList[1]
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(removedName)
        
        self.tempList[0].set(self.nameList[0])
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_2(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList
        print('place 2')
        removedName=self.nameList[1]
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(removedName)
        
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_3(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList
        print('place 3')
        removedName=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(removedName)
        
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_4(self,event):
        #need database(model) part, save remove information
        #need insert the removed name back to restList
        print('place 4')
        removedName=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        self.restList.remove(random_name)
        self.restList.append(removedName)
        
        self.tempList[3].set(random_name)
        
    #react qwer (*within 1 second after remove), mark flag symbol for removed student
    # qwer both are flag, so 1 func is enough?
    def flag(self,event):
        print("flag!")
    
    '''#test Terminal display
    def closeWin(self,event):
        print('place 5')
        self.fileMode=True
        self.app.destroy()'''

    def CCinterface(self):
        self.app.wm_attributes('-topmost',1)
        self.app.title('Cold-Call Assist')
        tk.Label(self.app, text='Next students:').pack(side='left')

        theLabel_1 = tk.Label(self.app, textvariable=self.tempList[0])
        theLabel_1.pack(side='left')
        self.app.bind("1",self.removeAndAddStudent_1)

        tk.Label(self.app, text=' ').pack(side='left')
		
        theLabel_2 = tk.Label(self.app, textvariable=self.tempList[1])
        theLabel_2.pack(side='left')
        self.app.bind("2",self.removeAndAddStudent_2)

        tk.Label(self.app, text=' ').pack(side='left')

        theLabel_3 = tk.Label(self.app, textvariable=self.tempList[2])
        theLabel_3.pack(side='left')
        self.app.bind("3",self.removeAndAddStudent_3)

        tk.Label(self.app, text=' ').pack(side='left')

        theLabel_4 = tk.Label(self.app, textvariable=self.tempList[3])
        theLabel_4.pack(side='left')
        self.app.bind("4",self.removeAndAddStudent_4)
        
        self.app.bind("q",self.flag)
        self.app.bind("w",self.flag)
        self.app.bind("e",self.flag)
        self.app.bind("r",self.flag)
        #self.app.bind("5",self.closeWin)

        print('done1')
		
        self.app.mainloop()
        
        '''#test Terminal display
        if self.fileMode==True:
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
        '''
        print('done2')



		
		








