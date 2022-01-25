#Python program to write a randomly generated number of students up to 20
#For cold call system
import sys
import random
#Bob	Jorginson	951584201	zcarroll@uoregon.edu	Zah-Kree	2587998
firstnames = ['Charlize', 'Téa', 'Amanda', 'Lupita', 'Idris', 'Rachel', 'Barbra', 'Gabourey', 'Martin', 'Isla', 'Saoirse', 'Joe', 'Joaquin', 'Demi', 'Ewan', 'Idina', 'Quvenzhané', 'Steve', 'Marion', 'Rihanna', 'Chloë', 'Alicia',
              'Ariana', 'Ralph', 'Milla', 'Shia', 'Sade', 'Zooey', 'Emily', 'Malin', 'Zach', 'Irina', 'Kaley', 'Camila', 'Princess', 'Gal', 'Milo', 'Cara', 'Doutzen', 'Chrissy']
phonetic =  ['Shar-LEES', 'Tay-UH', 'Uh-MAN-duh', 'LOO-pita', 'ID-riss', 'Ray-chul', 'Barb-RAH', 'GAB-or-ay', 'Mar-tin', 'EYE-luh',
             'SUR-sha', 'JO', 'Wah-KEEN', 'Duh-MEE', 'YOO-uhn', 'uh-dee-NUH', 'Kwah-ven-jah-NAY', 'Steev', 'Mah-ree-AHN',
             'Ree-AN-uh', 'KLO-ee', 'Ah-liss-ee-ah',
             'Are-ee-ana', 'Rae-fe', 'Mee-luh', 'Shy-a', 'Shah-DAY', 'ZOH-ee', 'Em-uh-lee', 'Mahl-in', 'Zak',
             'Eye-rena', 'Ka-lee', 'Cam-EE-la',
             'Prin-CESS', 'Gahl', 'My-low', 'Car-ah', 'Doubt-sen', 'Chris-EE']        
lastnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
             'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
             'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White',
             'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen',
             'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill','Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts']


def studentfile(num):
    #Chooses from the pool of names and chooses a random studentid/number to write into a file
    idlist = []
    numlist = []
    while (len(idlist) < num):
        studentid = random.randint(951000000, 952000000)
        if studentid not in idlist:
            idlist.append(studentid)
    while (len(numlist) < num):
        studentnum = random.randint(1000000, 9999999)
        if studentnum not in numlist:
            numlist.append(studentnum)
    space = " "
    domain = "@uoregon.edu"
    file = open("StudentFile.txt", "w")
    for i in range(0, num):
            x = random.randint(0,39)
            y = random.randint(0,49)
            fname = firstnames[x]
            phon = phonetic[x]
            lname = lastnames[y]
            email = fname[0]+lname+domain
            filestr = fname+"\t"+lname+"\t"+str(idlist[i])+"\t"+email.lower()+"\t"+phon+"\t"+str(numlist[i])+'\n'
            file.write(filestr)
    file.close()
"""
def student_creator():
    print("Enter a number of students to generate (Max:20): ")
    print("Enter 'stop' to end the program")
    inputnumber = 0
    for line in sys.stdin:
        if "stop" == line.rstrip():
            print("Program ending")
            break
        try:
            inputnumber = int(line)
        except:
            print("Only integers are allowed")
        if inputnumber > 100 or inputnumber < 1:
            print("Choose a number between 1 and 100")

        else:
            print("Generating student list in StudentFile.txt")
            studentfile(inputnumber)
            print("Finished")
            break
"""

def hundred_test_call():
    print("Are you sure you want to run 100 test calls? (Enter YES to confirm or any other key to quit)\nAny data in testoutputfile.txt will be deleted")
    for line in sys.stdin:
        if "YES" != line.rstrip() or "Yes" != line.rstrip() or "yes" != line.rstrip():
            f = open("testoutputfile.txt", 'w')
            print("Creating/Overwriting File")
            studentfile(100)
            f2 = open("StudentFile.txt", "r")
            students = []
            for thing in f2:
                students.append(thing.rstrip())

            queue = []
            for i in range(0,4):
                rand_int = random.randint(0, len(students))
                queue.append(students[rand_int])
                del students[rand_int]

            for i in range(0, 100):
                temp = random.choice(queue)
                queue.remove(temp)
                temp_two = random.choice(students)
                students.remove(temp_two)
                queue.append(temp_two)
                students.append(temp)
                student = temp.split()
                t = random.randint(0, 3)
                if t == 0:
                    student_to_write = "X    " + student[0] +" "+ student[1] +" "+ "<" + student[3] + ">"
                else:
                    student_to_write = student[0] +" "+ student[1] +" "+ "<" + student[3] + ">"
                #student_to_write = student[0] + "    " + student[1] + "    " + student[3]
                #student_to_write = f'{student[0]:{12}}    {student[1]:{12}}      {student[3]:{20}}'
                f.write(student_to_write + "\n")
            print("Test Finished")
            break

def main():
    hundred_test_call()
    #student_creator()

if __name__ == '__main__':
    main()
