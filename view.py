import tkinter as tk
import random


class UserInterface(object):

    def __init__(self, nameList,totalList):
        self.app = tk.Tk()
        self.nameList=nameList
        self.totalList=totalList
        tempList=[]
        for i in nameList:
            tempName=tk.StringVar()
            tempName.set(i)
            tempList.append(tempName)
        self.tempList=tempList
        
    def random_select(self):
        return random.choice(self.totalList)

    def removeAndAddStudent_1(self,event):
        print('place 1')
        self.nameList[0]=self.nameList[1]
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        
        self.tempList[0].set(self.nameList[0])
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_2(self,event):
        print('place 2')
        self.nameList[1]=self.nameList[2]
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        
        self.tempList[1].set(self.nameList[1])
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_3(self,event):
        print('place 3')
        self.nameList[2]=self.nameList[3]
        random_name=self.random_select()
        self.nameList[3]=random_name
        
        self.tempList[2].set(self.nameList[2])
        self.tempList[3].set(random_name)

    def removeAndAddStudent_4(self,event):
        print('place 4')
        random_name=self.random_select()
        self.nameList[3]=random_name
        
        self.tempList[3].set(random_name)

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

        print('done1')
		
        self.app.mainloop()

        print('done2')
		
#test
totalList=['name_1', 'name_2', 'name_3', 'name_4','name_5','name_6','name_7','name_8','name_9']
studentList=['Maria Diego', 'Anna Cavendish', 'Yunfeng Zhang', 'Aniyah Jackson']

interface=UserInterface(studentList,totalList)

interface.CCinterface()



		
		








