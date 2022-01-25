# Python functions that create random student data and store it in a file. It also randomly picks students and flags
# students randomly at a 25% chance.
# There is also a function that creates a warning page using tkinter
# These functions are used for the testing portion of the program
import sys
import random
import tkinter as tk
# Outline for how student data should be stored
# Example:Bob	Jorginson	951584201	zcarroll@uoregon.edu	Zah-Kree	2587998
# 70 first names along with the phonetic spellings
# 60 last names
firstnames = ['Charlize', 'Téa', 'Amanda', 'Lupita', 'Idris', 'Rachel', 'Barbra', 'Gabourey', 'Martin', 'Isla', 'Saoirse', 'Joe', 'Joaquin', 'Demi', 'Ewan', 'Idina', 'Quvenzhané', 'Steve', 'Marion', 'Rihanna', 'Chloë', 'Alicia',
              'Ariana', 'Ralph', 'Milla', 'Shia', 'Sade', 'Zooey', 'Emily', 'Malin', 'Zach', 'Irina', 'Kaley', 'Camila', 'Princess', 'Gal', 'Milo', 'Cara', 'Doutzen', 'Chrissy'
              ,'Kenny','Haowie','Britney','Tenzin','Ronny','Inho','Boowon','IraMae','Judy','Panda','Kacee','Konner'
              ,'Kurts','Nave','Kirk','Ansel','Lillian','Thao','Kim','Benny','Zed','Ezekeial','Yandis','Drake','Jax'
              ,'Desmond','Reeves','Wick','Ricola','Noah']

phonetic =  ['Shar-LEES', 'Tay-UH', 'Uh-MAN-duh', 'LOO-pita', 'ID-riss', 'Ray-chul', 'Barb-RAH', 'GAB-or-ay', 'Mar-tin', 'EYE-luh',
             'SUR-sha', 'JO', 'Wah-KEEN', 'Duh-MEE', 'YOO-uhn', 'uh-dee-NUH', 'Kwah-ven-jah-NAY', 'Steev', 'Mah-ree-AHN',
             'Ree-AN-uh', 'KLO-ee', 'Ah-liss-ee-ah',
             'Are-ee-ana', 'Rae-fe', 'Mee-luh', 'Shy-a', 'Shah-DAY', 'ZOH-ee', 'Em-uh-lee', 'Mahl-in', 'Zak',
             'Eye-rena', 'Ka-lee', 'Cam-EE-la',
             'Prin-CESS', 'Gahl', 'My-low', 'Car-ah', 'Doubt-sen', 'Chris-EE'
             ,'Can-E','How-E','Burit-NE','Ten-zen','Ron-E','In-hoe','Poo-won','I-rah-may','Joo-D','Pan-DAH','K-C','Cawn-ner'
             ,'Khurtz','Nay-v','Kurkh','An-sell','Lil-e-an','Tao','Ki-m','Ben-E','Z-edd','E-zeek-e-l','Yan-dis','Dra-k','Jah-x'
             ,'Des-mend','Ree-vs','Whi-ck','Ree-co-la','No-ah']

lastnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
             'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
             'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White',
             'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen',
             'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill','Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts'
             ,'Cao','Tran','Bui','Dugda','Pham','Chen','Le','Mae','Lieng','Ma']
#Total number of unique names in each list
allfn = len(firstnames)
allphone = len(phonetic)
allln = len(lastnames)

# function to create a file that stores students data
# the students data is generated randomly
def studentfile(num):
    # Chooses from the pool of names and chooses a random studentid/number to write into a file
    # and checks to see if there are any duplicates
    idlist = []
    numlist = []
    allnames = []
    while (len(allnames) < num): #Creates unique full name from list of names
        x = random.randint(0,allfn-1)
        y = random.randint(0,allln-1)
        currentname = [firstnames[x],phonetic[x],lastnames[y]]
        if currentname not in allnames:
            allnames.append(currentname)
    while (len(idlist) < num): #Creates a randomly generated unique student id
        studentid = random.randint(951000000, 952000000)
        if studentid not in idlist:
            idlist.append(studentid)
    while (len(numlist) < num): #Creates a randomly generated unique reveal code
        studentnum = random.randint(1000000, 9999999)
        if studentnum not in numlist:
            numlist.append(studentnum)

    # Generate email for each student
    space = " "
    domain = "@uoregon.edu"

    # Creates student and writes it to the file "StudentFile.txt"
    file = open("StudentFile.txt", "w")
    for i in range(0, num):
            fname = allnames[i][0]
            phon = allnames[i][1]
            lname = allnames[i][2]
            email = fname[0:3]+lname+domain
            filestr = fname+"\t"+lname+"\t"+str(idlist[i])+"\t"+email.lower()+"\t"+phon+"\t"+str(numlist[i])+'\n'
            file.write(filestr)
    file.close()

def caller():
    # This function generates random picking and 25% chance of flagging
    # Create file to write the output too
    f = open("testoutputfile.txt", 'w')

    # Generate random student data
    studentfile(100)
    f2 = open("StudentFile.txt", "r")

    # Create list of all the students
    students = []
    for thing in f2:
        students.append(thing.rstrip())

    # Create queue and choose randomly who joins the queue
    queue = []
    for i in range(0,4):
        rand_int = random.randint(0, len(students))
        queue.append(students[rand_int])
        del students[rand_int]

    # Goes through and picks randomly students from the queue and flags them randomly as well
    # In this for loop it also writes the output to "testouputfile.txt"
    for i in range(0, 100):
        # Choose randomly
        temp = random.choice(queue)
        queue.remove(temp)
        temp_two = random.choice(students)
        students.remove(temp_two)
        queue.append(temp_two)
        students.append(temp)
        student = temp.split()

        # 25% chance of being flagges
        t = random.randint(0, 3)

        # Write to file
        # Format is specified at the top of this file
        if t == 0:
            student_to_write = "X    " + student[0] +" "+ student[1] +" "+ "<" + student[3] + ">"
        else:
            student_to_write = student[0] +" "+ student[1] +" "+ "<" + student[3] + ">"
                #student_to_write = student[0] + "    " + student[1] + "    " + student[3]
                #student_to_write = f'{student[0]:{12}}    {student[1]:{12}}      {student[3]:{20}}'
        f.write(student_to_write + "\n")

    # Close files
    f.close()
    f2.close()


def testwarningInterface():
    # Generates tkinter window asking if user wants to go ahead with the test
    # Create tkinter window
    root = tk.Tk()
    root.geometry('+0+0')
    root.wm_attributes('-topmost', 1)

    # Create lables and titles for the window
    root.title('Warning')
    theLabel = tk.Label(root, fg='red', text='Test Warning! The test student data will be overwritten! Do you want to Continue?')
    theLabel.pack()
    button_1 = tk.Button(root, text='Continue',
                             command=lambda: [root.destroy(), caller()])
    button_1.pack()
    button_2 = tk.Button(root, text='Back', command=lambda: [root.destroy()])
    button_2.pack()
