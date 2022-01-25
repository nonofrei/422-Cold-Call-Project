import tkinter as tk
import random
from time import *
from ImportFile import *
from collections import *
from heapq import *

remove1 = '1'
remove2 = '2'
remove3 = '3'
remove4 = '4'

flag1 = 'q'
flag2 = 'w'
flag3 = 'e'
flag4 = 'r'


class UserInterface(object):

    def __init__(self, nameList, restList, data):
        self.nameList = []
        self.restList = []

        self.studentQueue = list()      # randomized priority queue
        self.infoMap = dict()           # hash map for storing student info
        self.classSize = 0              # for storing number of students

        self.fileMode = False
        if data == True:
            self.haveData = True
        else:
            self.haveData = False
        self.removedName = ''

        # for 1 sec flagging and avoiding double flagging
        self.keypress_timer = time()
        self.can_flag = True

    def removeAndAddStudent_1(self, event):
        # need database(model) part, save remove information
        # need insert the removed name back to restList

        # 1 sec delay and allow flagging
        self.keypress_timer = time()
        self.can_flag = True

        # remove corresponding student and increase their call counter
        # add them back to the priority queue
        self.removedName = self.nameList[0]
        self.removedName[0] += 1
        heappush(self.studentQueue, self.removedName)

        # slide students to the left on the display
        self.nameList[0] = self.nameList[1]
        self.nameList[1] = self.nameList[2]
        self.nameList[2] = self.nameList[3]

        # get next student from the priority queue
        nextStudent = heappop(self.studentQueue)
        self.nameList[3] = nextStudent

        # notify display to reflect the changes in the display names
        self.tempList[0].set(self.nameList[0][1])
        self.tempList[1].set(self.nameList[1][1])
        self.tempList[2].set(self.nameList[2][1])
        self.tempList[3].set(nextStudent[1])

    def removeAndAddStudent_2(self, event):
        # need database(model) part, save remove information
        # need insert the removed name back to restList

        # 1 sec delay and allow flagging
        self.keypress_timer = time()
        self.can_flag = True

        # remove corresponding student and increase their call counter
        # add them back to the priority queue
        self.removedName = self.nameList[1]
        self.removedName[0] += 1
        heappush(self.studentQueue, self.removedName)

        # slide names to the left on the display
        self.nameList[1] = self.nameList[2]
        self.nameList[2] = self.nameList[3]

        # get next student from the priority queue
        nextStudent = heappop(self.studentQueue)
        self.nameList[3] = nextStudent

        # notify display to reflect the changes in the display names
        self.tempList[1].set(self.nameList[1][1])
        self.tempList[2].set(self.nameList[2][1])
        self.tempList[3].set(nextStudent[1])

    def removeAndAddStudent_3(self, event):
        # need database(model) part, save remove information
        # need insert the removed name back to restList

        # 1 sec delay and allow flagging
        self.keypress_timer = time()
        self.can_flag = True

        # remove corresponding student and increase their call counter
        # add them back to the priority queue
        self.removedName = self.nameList[2]
        self.removedName[0] += 1
        heappush(self.studentQueue, self.removedName)

        # slide names to the left on the display
        self.nameList[2] = self.nameList[3]

        # get next student from the priority queue
        nextStudent = heappop(self.studentQueue)
        self.nameList[3] = nextStudent

        # notify display to reflect the changes in the display names
        self.tempList[2].set(self.nameList[2][1])
        self.tempList[3].set(nextStudent[1])

    def removeAndAddStudent_4(self, event):
        # need database(model) part, save remove information
        # need insert the removed name back to restList

        # 1 sec delay and allow flagging
        self.keypress_timer = time()
        self.can_flag = True

        # remove corresponding student and increase their call counter
        # add them back to the priority queue
        self.removedName = self.nameList[3]
        self.removedName[0] += 1
        heappush(self.studentQueue, self.removedName)

        # get next student from priority queue
        nextStudent = heappop(self.studentQueue)
        self.nameList[3] = nextStudent

        # notify display to reflect the changes in the display names
        self.tempList[3].set(nextStudent[1])

    def flag(self, event):
        time_difference = time() - self.keypress_timer

        # within 1 sec and can flag
        if time_difference <= 1 and self.can_flag:
            print("flag:", self.removedName)

        # no more flags till next student removed
        self.can_flag = False

    def inputFile(self):
        if self.haveData == False:
            ImportFile()
            self.haveData = True
        else:
            self.warningInterface()

    def confirmInput(self):
        ImportFile()
        self.haveData = True

    def outputFile(self):
        ExportFile()

    '''def clearData(self):
        print('Clear all student data')
        self.haveData = False'''

    # initial view
    def firstInterface(self):
        root = tk.Tk()
        root.geometry('250x90+0+0')
        root.wm_attributes('-topmost', 1)
        root.title('Model select')
        button_1 = tk.Button(root, text='Cold Call Assist', command=lambda: [root.destroy(), self.CCinterface()])
        button_1.pack()

        button_2 = tk.Button(root, text='Import New File', command=lambda: self.inputFile())
        button_2.pack()

        button_3 = tk.Button(root, text='Export Existing File', command=lambda: self.outputFile())
        button_3.pack()

        root.mainloop()

    '''#tkinter window have been closed, now in termial
    def fileInterface(self):
        root=tk.Tk()
        root.geometry('+0+0')
        root.wm_attributes('-topmost',1)
        root.title('File operation')
        entry = tk.Entry(root, bd =5)
        entry.grid(row=0,column=1)
        self.entry=entry
        button_1=tk.Button(root,text='Input',command=lambda:self.inputFile(self.entry))
        button_1.grid(row=1,column=0)
        button_2=tk.Button(root,text='Output',command=lambda:self.outputFile(self.entry))
        button_2.grid(row=1,column=2)
        button_3=tk.Button(root,text='Back',command=lambda:[root.destroy(),self.firstInterface()])
        button_3.grid(row=2,column=1)
        root.mainloop()

    def exportFileInterface(self):
        root = tk.Tk()
        root.geometry('+0+0')
        root.wm_attributes('-topmost', 1)
        root.title('Export file')
        entry = tk.Entry(root, bd=5)
        entry.pack()
        self.entry = entry
        button_1 = tk.Button(root, text='Export', command=lambda: self.outputFile(self.entry))
        button_1.pack()
        button_2 = tk.Button(root, text='Back', command=lambda: [root.destroy()])
        button_2.pack()
        root.mainloop()'''

    def warningInterface(self):
        root = tk.Tk()
        root.geometry('+0+0')
        root.wm_attributes('-topmost', 1)
        root.title('Warning')
        theLabel = tk.Label(root, fg='red', text='Warning! Already existing students data, do you want to cover it?')
        theLabel.pack()
        button_1 = tk.Button(root, text='Continue',
                             command=lambda: [root.destroy(), self.confirmInput()])
        button_1.pack()
        button_2 = tk.Button(root, text='Back', command=lambda: [root.destroy()])
        button_2.pack()

    # cold call view
    def CCinterface(self):
        # check if there is a saved file with student info
        try:
            currentRoster = open("CurrentRoster.txt", "r")
        except:
            FileError("No Existing Student List", "Please Import Student List")
            return

        # process student list file
        self.restList = deque(ScanFile(currentRoster, True))

        # check that it read the file correctly
        if self.restList.popleft() == "E":
            FileError("Error Reading Current Student List", "Please Import New Student List")
            return

        # create random queue and hash map with information
        self.classSize = len(self.restList)
        for i in range(self.classSize):
            student = random.choice(self.restList)
            name = student[0] + " " + student[1]
            heappush(self.studentQueue, [0, name])
            self.infoMap[name] = student
            self.restList.remove(student)

        # add 4 students to the display list
        for i in range(4):
            self.nameList.append(heappop(self.studentQueue))

        # create window
        self.app = tk.Tk()
        self.app.geometry('+0+0')

        tempList = []
        for i in self.nameList:
            tempName = tk.StringVar()
            tempName.set(i[1])
            tempList.append(tempName)
        self.tempList = tempList

        self.app.wm_attributes('-topmost', 1)
        self.app.title('Cold-Call Assist')
        tk.Label(self.app, text='Next students:').grid(row=0, column=0)

        theLabel_1 = tk.Label(self.app, textvariable=self.tempList[0])
        theLabel_1.grid(row=0, column=1)
        self.app.bind(remove1, self.removeAndAddStudent_1)

        tk.Label(self.app, text=' ').grid(row=0, column=2)

        theLabel_2 = tk.Label(self.app, textvariable=self.tempList[1])
        theLabel_2.grid(row=0, column=3)
        self.app.bind(remove2, self.removeAndAddStudent_2)

        tk.Label(self.app, text=' ').grid(row=0, column=4)

        theLabel_3 = tk.Label(self.app, textvariable=self.tempList[2])
        theLabel_3.grid(row=0, column=5)
        self.app.bind(remove3, self.removeAndAddStudent_3)

        tk.Label(self.app, text=' ').grid(row=0, column=6)

        theLabel_4 = tk.Label(self.app, textvariable=self.tempList[3])
        theLabel_4.grid(row=0, column=7)
        self.app.bind(remove4, self.removeAndAddStudent_4)

        buttonBack = tk.Button(self.app, text='Back', command=lambda: [self.app.destroy(), self.firstInterface()])
        buttonBack.grid(row=1, sticky='w')

        self.app.bind(flag1, self.flag)
        self.app.bind(flag2, self.flag)
        self.app.bind(flag3, self.flag)
        self.app.bind(flag4, self.flag)

        self.app.mainloop()
