import tkinter as tk
import random
from viewAndController import *
#from model import *

def main():
    #some step here, need to get studnet data from model, and by a algorithm, ramdomly select 4 students from inputed .csv file, put into a list, and rest of student in another list (studentList+restList=totalList)
    studentList=['Maria Diego', 'Anna Cavendish', 'Yunfeng Zhang', 'Aniyah Jackson']
    restList=['name_1', 'name_2', 'name_3', 'name_4','name_5','name_6','name_7','name_8','name_9']
    
    interface=UserInterface(studentList,restList)
    interface.CCinterface()
    #!!!interface.CCinterface() must be the last step of main(), because before the cold call windows close, not code run behind the line self.app.mainloop() in func CCinterface()

if __name__ == '__main__':
    main()

		
		








