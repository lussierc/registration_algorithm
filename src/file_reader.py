"""Holds the function that reads in the text file containing the students and
their information regarding their registration."""

# Authors: Christian Lussier, Ben Watto, Mikey Spurr
# "All work is our own unless otherwise cited.""

def registrationList_processor(file_name):
    """Function to read in the student information"""

    types = str, str, str, float, int # set the types of each item being read in

    try:
        with open(file_name, "r") as file:  # opening file to be parsed
            stu_registationList = []  # create stu_registationList to store student data
            for line in file:  # parsing through the file
                elements = tuple(t(e) for t,e in zip(types, line.split("; ")))  # splitting up the data for student info, each students information is stored into a seperate tuple
                stu_registationList.append(elements)  # add tuples of song data to list
        return(stu_registationList)
    except:
        print("File inputting failed. Please enter a valid input file.")
