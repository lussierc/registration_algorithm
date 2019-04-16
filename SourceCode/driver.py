# Christian Lussier, Ben Watto, Mikey Spurr
# This file will hold the driver code for the program
from fileReader import *
from organizer import *
#from organizer import letter_group_organizer

def main():
    """Driver program of the project."""
    # Print welcome message:
    print("*************************************************************")
    print("* Thanks for using our Registration Letter Group Organizer! *")
    print("*************************************************************")

    #file_name = input("Please enter a file name to use:   ")

    currentgroups = ["A", "B", "C", "F", "E", "D", "H", "G"]
    student_list = registrationList_processor()
    #print([x[2] for x in student_list])

    letter_group_organizer(currentgroups, student_list)

main()
