"""https://www.codewars.com/kata/5648b12ce68d9daa6b000099"""

# Number of People in the Bus

def number(bus_stops):
    all_people = 0
    for i in bus_stops:
        all_people += i[0] - i[1]
    return max( all_people, 0)
