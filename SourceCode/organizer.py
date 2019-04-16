# Christian Lussier, Ben Watto, Mikey Spurr
# This file will hold the program's algorithm
from itertools import chain
import random

def letter_group_organizer(letter_groups):
    """Letter Group Organizer Algorithm"""
    # split in half
    second_half = letter_groups[:len(letter_groups)//2]
    first_half = letter_groups[len(letter_groups)//2:]
    print("FIRST:", first_half)
    print("SECOND:", second_half)

    #split into subhalves/quarters
    first_half_quarter1 = first_half[:len(first_half)//2]
    print("SUB1:", first_half_quarter1)
    first_half_quarter2 = first_half[len(first_half)//2:]
    print("SUB2:", first_half_quarter2)
    second_half_quarter1 = second_half[:len(second_half)//2]
    print("SUB3:", second_half_quarter1)
    second_half_quarter2 = second_half[len(second_half)//2:]
    print("SUB4:", second_half_quarter2)

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

    print(all_groups)

    # for list in BIGLIST:
    #     # calculate avg gpa for groups
    #     acv_gpa = sum(list)
    #     if list1gpa < list2gpa:
    #         #swap
    #         swapme
    #     else:
    #         no swap
    # # sort by GPA

currentgroups = ["A", "B", "C", "F", "E", "I", "H", "G"]
letter_group_organizer(currentgroups)
