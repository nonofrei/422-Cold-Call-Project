import tkinter as tk
import random
from time import *
from datetime import datetime
from threading import Thread
import os

import Testing
from ImportAndExport import *
from collections import *
from heapq import *
from Testing import *

remove1 = '1'
remove2 = '2'
remove3 = '3'
remove4 = '4'

flag1 = 'q'
flag2 = 'w'
flag3 = 'e'
flag4 = 'r'

test_key = 't'


class UserInterface(object):

    def __init__(self):
        self.nameList = []
        self.restList = []

        self.studentQueue = list()      # randomized priority queue
        self.infoMap = dict()           # hash map for storing student info
        self.classSize = 0              # for storing number of students

        self.fileMode = False
        self.removedName = ''

        # for 1 sec flagging and avoiding double flagging
        self.keypress_timer = time()
        self.can_flag = True
        self.test_flag = False

    def print_summary_line(self):
        sleep(1)
        studentInfo = self.infoMap[self.removedName[1]]
        output = studentInfo[0] + "\t" + studentInfo[1] + "\t<" + studentInfo[3] + ">\n"
        if not self.can_flag:
            output = "X\t" + output
        self.summaryFile.write(output)


    def removeAndAddStudent_1(self, event):

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

        # print to output file, use a separate thread so that our main thread
        # is not waiting on if the flagging occurs
        thread = Thread(target=self.print_summary_line)
        thread.start()

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

        # print to output file, use a separate thread so that our main thread
        # is not waiting on if the flagging occurs
        thread = Thread(target=self.print_summary_line)
        thread.start()

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

        # print to output file, use a separate thread so that our main thread
        # is not waiting on if the flagging occurs
        thread = Thread(target=self.print_summary_line)
        thread.start()

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

        # print to output file, use a separate thread so that our main thread
        # is not waiting on if the flagging occurs
        thread = Thread(target=self.print_summary_line)
        thread.start()

    def flag(self, event):
        time_difference = time() - self.keypress_timer

        # within 1 sec and can flag
        if time_difference <= 1 and self.can_flag:
            self.can_flag = False

    def test_flagging(self, event):
        # test_flagging checks to see if the 't' key has already been pressed once
        # If it has then it calls initiate_testing
        # If not then it sets the test_flag to True
        if self.test_flag == False:
            self.test_flag = True
            return

        if self.test_flag:
            self.initiate_testing()
            self.test_flag = False

    def initiate_testing(self):
        # This method calls on test_warningInterface to initiate the testing procedure
        if self.test_flag:
            studentgen.testwarningInterface()
        self.test_flag = False

    def inputFile(self):
        if os.path.exists('CurrentRoster.txt') == False:
            ImportFile()
        else:
            self.warningInterface()

    def confirmInput(self):
        ImportFile()

    def outputFile(self):
        ExportFile()

    # initial view
    def firstInterface(self):
        self.app = tk.Tk()
        self.app.geometry('250x90+0+0')
        self.app.wm_attributes('-topmost', 1)
        self.app.title('Model select')
        button_1 = tk.Button(self.app, text='Cold Call Assist', command=lambda: [self.CCinterface()])
        button_1.pack()

        button_2 = tk.Button(self.app, text='Import New File', command=lambda: self.inputFile())
        button_2.pack()

        button_3 = tk.Button(self.app, text='Select Location to Export Student File', command=lambda: self.outputFile())
        button_3.pack()

        self.app.mainloop()

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

        # create summary file to write to
        now = datetime.now()
        fileName = now.strftime("%b-%d-%Y_%H:%M:%S") + "_Summary.txt"
        self.summaryFile = open(fileName, "w")

        # we can now safely close the main menu, open cold call assist
        self.app.destroy()

        # create window
        root = tk.Tk()
        root.geometry('+0+0')

        tempList = []
        for i in self.nameList:
            tempName = tk.StringVar()
            tempName.set(i[1])
            tempList.append(tempName)
        self.tempList = tempList

        root.wm_attributes('-topmost', 1)
        root.title('Cold-Call Assist')
        tk.Label(root, text='Next students:').grid(row=0, column=0)

        theLabel_1 = tk.Label(root, textvariable=self.tempList[0])
        theLabel_1.grid(row=0, column=1)
        root.bind(remove1, self.removeAndAddStudent_1)

        tk.Label(root, text=' ').grid(row=0, column=2)

        theLabel_2 = tk.Label(root, textvariable=self.tempList[1])
        theLabel_2.grid(row=0, column=3)
        root.bind(remove2, self.removeAndAddStudent_2)

        tk.Label(root, text=' ').grid(row=0, column=4)

        theLabel_3 = tk.Label(root, textvariable=self.tempList[2])
        theLabel_3.grid(row=0, column=5)
        root.bind(remove3, self.removeAndAddStudent_3)

        tk.Label(root, text=' ').grid(row=0, column=6)

        theLabel_4 = tk.Label(root, textvariable=self.tempList[3])
        theLabel_4.grid(row=0, column=7)
        root.bind(remove4, self.removeAndAddStudent_4)

        buttonBack = tk.Button(root, text='Back', command=lambda: [root.destroy(), self.firstInterface()])
        buttonBack.grid(row=1, sticky='w')

        root.bind(flag1, self.flag)
        root.bind(flag2, self.flag)
        root.bind(flag3, self.flag)
        root.bind(flag4, self.flag)

        # Bind the test key to the appropiate method
        root.bind(test_key, self.test_flagging)

        root.mainloop()

# initiate cold call system
def main():
    interface=UserInterface()
    interface.firstInterface()

if __name__ == '__main__':
    main()