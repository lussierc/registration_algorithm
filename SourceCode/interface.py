# Christian Lussier, Ben Watto, Mikey Spurr
# This file will hold the driver code for the program
from fileReader import *
from organizer import *
import time
#from organizer import letter_group_organizer

def main():
    """Driver program of the project."""
    # Print welcome message:
    print("*************************************************************")
    print("* Thanks for using our Registration Letter Group Organizer! *")
    print("*************************************************************")
    print()

    file_name = input("Sample input file example: ../input/sample_students.txt \n*** Please enter a file name to use:   ")

    print()

    currentgroups = ["A", "B", "C", "F", "E", "D", "H", "G"]

    print()
    print("Previous Letter Group Order:", currentgroups)
    print()
    try:
        student_list = registrationList_processor(file_name)
        #print([x[2] for x in student_list])

        start_time = time.time()  # start timer
        sorted_students = letter_group_organizer(currentgroups, student_list)
        stop_time = time.time()  # stop timer
        time_elapsed = stop_time - start_time  # calculate function run time
        print("** It took the program this long to run:", time_elapsed)

        print()
        chosen_file_name = input("Sample output file example: ../output/output.txt \n*** Please enter a file name to output sorted student info to:   ")

        print()
         # file name to output to
        output_file = open(chosen_file_name,'w') # opens previously created file, creates new file if necessary
        print() # print blank line for spacing
        print() # print blank line for spacing
        print("{:<30}{:<25}{:<20}{:<15}\n".format("Student Name", "Class Year", "Letter Group", "GPA")) # print output header
        output_file.write("{:<30}{:<25}{:<20}{:<15}".format("Student Name", "Class Year", "Letter Group", "GPA"))
        for ele1,ele2,ele3,ele4 in sorted_students:
            print("{:<30}{:<25}{:<20}{:<15}".format(ele1,ele2,ele3,ele4))
            output_file.write("\n{:<30}{:<25}{:<20}{:<15}".format(ele1,ele2,ele3,ele4))
        output_file.close()
    except:
        print("\n Exiting....")
main()
