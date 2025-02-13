"""https://www.codewars.com/kata/514a6336889283a3d2000001/train/python"""

# Check the exam

def check_exam(arr1,arr2):
    check = 0
    for correct_ans, stud_ans in zip(arr1,arr2):
        if stud_ans.strip() == "":
            continue
        elif stud_ans == correct_ans:
            check += 4
        else:
            check -= 1
    return max(check, 0)