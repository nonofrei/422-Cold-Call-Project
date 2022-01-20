from tkinter import filedialog, Text


"""
    This function provides the functionality for the import file button. It opens a file searching window and allows
    the user to search their computer for their desired file. They are only allowed to select .txt files within this 
    window that pops up. Once the file has been selected the specified format is checked for and if the format is
    incorrect then the function will return information about the error encountered to the caller 
    (see return value) below.
                                --------------------------------------------

        filePath: Varaible which contains the path name for the file selected from the pop up window, uses tkinter 
                  library
         
         scanRes: Variable containing the result of the format checking
         
         newFile: File pointer for the copied roster
         
    return value: Returns a tuple (<Line Number>, <Error string>), if the tuple (0,0) is returned then the action
                  was successful and the file has been successfully imported
"""
def ImportFile():

    # Ask user for to browse for their file
    # use tkinter library to avoid OS specific approach to open a file selection window and save the path of the file
    filePath = filedialog.askopenfilename(initialdir="/", title="Select Import File",
                                      filetypes=(("text", "*.txt"), ("all files", "*.*")))

    # Try to open file safely
    try:

        f = open(filePath, "r")

    # Problem on OS side return error string
    except OSError as err:

        return "Unable to open file:", err.strerror

    scanRes = ScanFile(f, False)

    # If file not in correct format then return the error strings (<Error on line>, <Component with error>)
    if scanRes[0] != 0:
        return scanRes

    newFile = open("CurrentRoster.txt", "w")

    f.seek(0)  # Reset file pointer to beginning of file

    # Copy file to working directory
    for line in f.readlines():
        newFile.write(line)

    f.close()
    newFile.close()
    return (0,0)

"""
    This function will return values based on the value of returnStudentList. If this value is True then ScanFile will
    return a list. Contained in this list will be lists of individual student information. The format of the return 
    value is ["E", <Error Message>] or ["L", [<First Name>, <Last Name>...] .... [<First Name>, <Last Name>...]].
    When using this function before proceeding with return values you need to check what the first value in the list is
    and act accordingly.
"""

def ScanFile(f, returnStudentList):

    errorDict = {
        -1: "First or last name contained invalid character",
        -2: "Problem with UO ID",
        -3: "Problem with email address",
        -4: "Reveal code contains non-numeric characters",
        -7: "Contained invalid white-space character",
        -8: "Line is missing information"
    }

    studentInfoLists = []
    studentInfoLists.append("L")

    for lnum, line in enumerate(f.readlines()):

        student = []
        splitLine = line.split("\t")

        # analyze each individual line in the file for correctness
        for cnum, comp in enumerate(splitLine):

            """
            here we will return a tuple containing the line number the error was found on
            and the component which contained the issue
            """
            # check for proper amount of components
            if(len(splitLine) < 5):
                return ["E", f"Error on line {lnum}: {errorDict[-8]}"]

            # if space is found then file tabbing was done in correctly
            if comp.find(" ") > -1:
                return ["E", f"Error on line {lnum}: {errorDict[-7]}"]

            # check first and last name with same method
            elif cnum == 0 or cnum == 1:
                if not comp.isalpha():
                    return ["E", f"Error on line {lnum}: {errorDict[-1]}"]

            # check UO ID must be a number 9 digits long and start with 951
            elif cnum == 2:
                if not comp.isdigit() or len(comp) != 9 or comp.find("951", 0, 3) == -1:
                    return ["E" ,f"Error on line {lnum}: {errorDict[-2]}"]

            # check email for @ and . not very robust check but works for now
            # TODO: Possibly add regex check for email validity
            elif cnum == 3:
                if comp.find("@") == -1 or comp.find(".") == -1:
                    return ["E", f"Error on line {lnum}: {errorDict[-3]}"]

            # TODO: Possibly add regex check for phonetic spelling validity here

            # file may not contain phonetic spellings so find out what the 5th component is
            elif cnum >= 4:
                if len(splitLine) == 5: # if true then this is a reveal code
                    if not comp.isdigit():
                        return ["E", f"Error on line {lnum}: {errorDict[-4]}"]



            student.append(comp)

        studentInfoLists.append(student)

    if returnStudentList:
        return studentInfoLists

    else:
        return (0,0)

ImportFile()