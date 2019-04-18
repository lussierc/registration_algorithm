"""Process in the text file containing the students and their information regarding their registration"""
# Christian Lussier, Ben Watto, Mikey Spurr
# This work is ours unless otherwise cited.
import pprint
def registrationList_processor(file_name):
    """Function to read in the student information"""
    #file_name = "../input/sample_students.txt" #finding the populated file

    types = str, str, str, float, int # set the types of each item being read in

    with open(file_name, "r") as file: # opening file to be parsed
        stu_registationList = [] # create stu_registationList to store student data
        for line in file: # parsing through the file
            elements = tuple(t(e) for t,e in zip(types, line.split("; "))) # splitting up the data for student info, each students information is stored into a seperate tuple
            stu_registationList.append(elements) # add tuples of song data to list
    return(stu_registationList)
