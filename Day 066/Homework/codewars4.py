"""https://www.codewars.com/kata/5c2b4182ac111c05cf388858/train/python"""

# Read the time

def solve(time):
    h = ["midnight", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine", "ten", "eleven", "midnight"]
    
    m = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
        "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    
    hour, minute = map(int,time.split(":"))
    if minute == 0:
        if hour == 0:
            return "midnight"
        return h[hour] + " o'clock"
    if minute == 15:
        return "quarter past " + h[hour]
    if minute == 45:
        return "quarter to " + h[1 + hour]
    if minute == 30:
        return "half past " + h[hour]
    if minute == 1:
        return "one minute past " + h[hour]
    if minute == 59:
        return "one minute to " + h[1 + hour]
    if int(int(minute) < 30):
        return m[minute] + " minutes past " + h[hour]
    return m[60 - minute] + " minutes to " + h[1 + hour]

        
