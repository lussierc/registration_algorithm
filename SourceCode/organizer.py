# Christian Lussier, Ben Watto, Mikey Spurr
# This file will hold the program's algorithm
from itertools import chain
import random
import pprint

def letter_group_organizer(letter_groups, students):
    """Letter Group Organizer Algorithm"""
    # split in half
    print("Previous Letter Group Order:", letter_groups)
    second_half = letter_groups[:len(letter_groups)//2]
    first_half = letter_groups[len(letter_groups)//2:]

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
    all_groups = []
    all_groups.append(first_half)
    all_groups.append(second_half)

    # Sort letter groups:
    for half in all_groups:
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

        # Organize letter groups in subhalves by higher GPA:
        for subhalve in half:
            shalve1_gpa = 0
            shalve2_gpa = 0
            student_len = len(students)
            for i in range(student_len):
                student1 = str(students[i][2])
                student_ltr = student1.replace(" ", "") # remove spaces around letter
                subhalve1 = str(subhalve[0])
                subhalve2 = str(subhalve[1])

                if student_ltr == subhalve1:
                    print("TEST - ", subhalve1, students[i][3]) # for testing
                    temp0 = temp0 + students[i][3]
                    counter0 += 1
                    shalve1_gpa = temp0 / counter0
                elif student_ltr == subhalve2:
                    print("TEST2 -", subhalve2, students[i][3])
                    temp1 = temp1 + students[i][3]
                    counter1 += 1
                    shalve2_gpa = temp1 / counter1
                else:
                    continue
            if shalve1_gpa < shalve2_gpa:
                print("swap")
                temp = subhalve[0]
                subhalve[0] = subhalve[1]
                subhalve[1] = temp


    # Combine letter group sublists back into one list.
    final_groups = []
    for half in all_groups:
        for subhalve in half:
            final_groups += subhalve
    print(final_groups)

    sorted_students = []
    SR_group = []
    JR_group = []
    SO_group = []
    FR_group = []
    for group in final_groups:
        for i in range(len(students)):
            student_ltr = str(students[i][2])
            student_yr = str(students[i][1])
            student_priority = int(students[i][-1])

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

    # student_classes = []
    # student_classes.append(SR_group)
    # student_classes.append(JR_group)
    # student_classes.append(SO_group)
    # student_classes.append(FR_group)
    # for stnt_class in student_classes:
    #     length = len(stnt_class)
    #     for x in range(length):
    #         for j in range(x+1, length):
    #             if stnt_class[x-1][-1] < stnt_class[j][-1]:
    #                 temp = stnt_class[x-1]
    #                 stnt_class[x-1] = stnt_class[j]
    #                 stnt_class[j] = temp
    #             else:
    #                 pass

    sorted_students = SR_group + JR_group + SO_group + FR_group # add classes back into one sorted/final group

    return(sorted_students)
