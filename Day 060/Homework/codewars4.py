"""https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python"""

# Grasshopper - Grade book

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'