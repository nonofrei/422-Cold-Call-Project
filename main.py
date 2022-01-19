import tkinter as tk
import random
from viewAndController import *
#from model import *

def main():
    #some step here, need to get studnet data from model, and by a algorithm, ramdomly select 4 students from inputed .csv file, put into a list, and rest of student in another list (studentList+restList=totalList)
    studentList=['Maria Diego', 'Anna Cavendish', 'Yunfeng Zhang', 'Aniyah Jackson']
    restList=['name_1', 'name_2', 'name_3', 'name_4','name_5','name_6','name_7','name_8','name_9']
    
    #existData tells view is there data in database or not when user open program
    #existData=True
    existData=False
    interface=UserInterface(studentList,restList,existData)
    interface.firstInterface()

if __name__ == '__main__':
    main()

		
		








