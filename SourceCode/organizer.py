# Christian Lussier, Ben Watto, Mikey Spurr
# This file will hold the program's algorithm
from itertools import chain
import random

def letter_group_organizer(letter_groups, students):
    """Letter Group Organizer Algorithm"""
    # split in half
    print("Previous Letter Group Order:", letter_groups)
    second_half = letter_groups[:len(letter_groups)//2]
    first_half = letter_groups[len(letter_groups)//2:]

    #split into subhalves/quarters
    first_half_quarter1 = first_half[:len(first_half)//2]
    first_half_quarter2 = first_half[len(first_half)//2:]
    second_half_quarter1 = second_half[:len(second_half)//2]
    second_half_quarter2 = second_half[len(second_half)//2:]

    first_half = []
    first_half.append(first_half_quarter1)
    first_half.append(first_half_quarter2)
    second_half = []
    second_half.append(second_half_quarter1)
    second_half.append(second_half_quarter2)
    all_groups = []
    all_groups.append(first_half)
    all_groups.append(second_half)

    for half in all_groups:
        temp = []
        if random.randint(0,100) < 50:
            temp = half[0]
            half[0] = half[1]
            half[1] = temp
        #### IN PROGRESS:
        for subhalve in half:
            student_len = len(students)
            for i in range(student_len):
                print(students[i][2], "vs", subhalve[0], "&", subhalve[1])
                if str(students[i][2]) == str(subhalve[0]):
                    print("yup")
                    temp0 = temp0 + students[i][3]
                    counter += 1
                    shalve1_gpa = temp0 / counter
                elif students[i][2] == subhalve[1]:
                    print("yup")
                    temp0 = temp0 + students[i][3]
                    counter += 1
                    shalve2_gpa = temp0 / counter
                else:
                    print("test")

                # if students[key] == subhalve[0]:
                # # if subhalve[0].gpa < subhalve[1].gpa:
                # #     temp = subhalve[0]
                # #     subhalve[0] = subhalve[1]
                # #     subhalve[1] = temp
                # else:
                #     continue

    print(all_groups)
