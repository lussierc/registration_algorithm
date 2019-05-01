"""This file holds the program's algorithm."""

# Authors: Christian Lussier, Ben Watto, Mikey Spurr
# "All work is our own unless otherwise cited.""

import random

def letter_group_organizer(letter_groups, students):
    """Letter Group Organizer and Student Sorting Algorithm."""

    print()
    print("--------------------------------------------------------------")
    print("Detailing the steps the algorithm is taking below:")
    print()

    # split in half:
    second_half = letter_groups[:len(letter_groups)//2]
    first_half = letter_groups[len(letter_groups)//2:]
    # Output current steps being taken:
    print("Splitting letter group order into halves and swapping halves:")
    print("First half:", first_half)
    print("Second half:", second_half)
    print()  # blank line for spacing


    # Split into subhalves/quarters:
    first_half_quarter1 = first_half[:len(first_half)//2]
    first_half_quarter2 = first_half[len(first_half)//2:]
    second_half_quarter1 = second_half[:len(second_half)//2]
    second_half_quarter2 = second_half[len(second_half)//2:]

    # Add the now seperated quarters into their respective halves:
    first_half = []
    first_half.append(first_half_quarter1)
    first_half.append(first_half_quarter2)
    second_half = []
    second_half.append(second_half_quarter1)
    second_half.append(second_half_quarter2)
    # Output current steps being taken:
    print("Splitting halves into subhalves/quarters:")
    print("First Half with Subhalves:", first_half)
    print("Second Half with Subhalves:", second_half)
    print()  # print blank line for spacing

    # put everything back in one list:
    all_groups = []
    all_groups.append(first_half)
    all_groups.append(second_half)

    # Sort letter groups:
    for half in all_groups:
        print("Entering a new half.")
        # initialize holder variables
        temp0 = 0
        temp1 = 0
        counter0 = 0
        counter1 = 0
        temp = []

        # Randomly swap subhalves:
        if random.randint(0,100) < 50:
            temp = half[0]
            half[0] = half[1]
            half[1] = temp
            print("Randomly swapping subhalves within half:")
            print(half[1], "moves in front of", half[0])
            print()

        # Organize letter groups in subhalves by higher GPA:
        print("Calculating average GPA for each letter group in the current half.")
        for subhalve in half:
            shalve1_gpa = 0
            shalve2_gpa = 0
            student_len = len(students)
            for i in range(student_len):
                student1 = str(students[i][2])
                student_ltr = student1.replace(" ", "") # remove spaces around letter if necessary
                subhalve1 = str(subhalve[0])
                subhalve2 = str(subhalve[1])

                if student_ltr == subhalve1:
                    temp0 = temp0 + students[i][3]
                    counter0 += 1
                    shalve1_gpa = temp0 / counter0
                elif student_ltr == subhalve2:
                    temp1 = temp1 + students[i][3]
                    counter1 += 1
                    shalve2_gpa = temp1 / counter1
                else:
                    continue
            if shalve1_gpa < shalve2_gpa:
                temp = subhalve[0]
                subhalve[0] = subhalve[1]
                subhalve[1] = temp
                print("Moving group in subhalf with higher GPA to the front of the list:", subhalve[0])
                print("Moving group in subhalf with higher GPA to the front of the list:", subhalve[1])
                print()

    # Combine letter group sublists back into one list.
    final_groups = []
    for half in all_groups:
        for subhalve in half:
            final_groups += subhalve
    print()
    print("Sorted Letter Groups:", final_groups)

    print()
    print("Sorting students based on class an new letter group order.")
    print("Algorithm is done running!")
    print("--------------------------------------------------------------")
    print()
    print()
    print("Sorted Letter Groups:", final_groups)

    sorted_students = []
    SR_group = []
    JR_group = []
    SO_group = []
    FR_group = []
    for group in final_groups:
        for i in range(len(students)):
            student_ltr = str(students[i][2])
            student_yr = str(students[i][1])

            # if the current student is apart of the class, add them to their class's list:
            if student_ltr == group:
                if student_yr == "SR":
                    SR_group.append(students[i])
                elif student_yr == "JR":
                    JR_group.append(students[i])
                elif student_yr == "SO":
                    SO_group.append(students[i])
                elif student_yr == "FR":
                    FR_group.append(students[i])
                else:
                    continue
            else:
                continue


    sorted_students = SR_group + JR_group + SO_group + FR_group # add classes back into one sorted/final group

    return(sorted_students)
