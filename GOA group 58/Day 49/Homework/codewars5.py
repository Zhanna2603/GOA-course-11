"""https://www.codewars.com/kata/5a1dc4baffe75f270200006b"""

 # Only Duplicates

def only_duplicates(st):
    result = ""
    for i in st:
        if st.count(i) > 1:
            result += i 
    return result