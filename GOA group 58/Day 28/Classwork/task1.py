# def solution(number):
#     sum = 0
    
#     for num in range(1, number):
#         if num % 3 == 0 or num % 5 == 0:
#             sum += num
#     return sum



# def get_middle(s):
#     s_len = len(s)
#     middle_char = s_len // 2
#     if s_len % 2 == 0:
#         return s[middle_char -1: middle_char + 1]
#     return s[middle_char]



# def say_hi(name):
#     print("Hello" + name)
# say_hi("Mari")



# def say_hi(name):
#     return("Hello" + name)
# print(say_hi("Mari"))


# def high_and_low(numbers):
#     splited_numbers = []
#     string1 = ""
    
#     for i in numbers + " ":
#         if i == " ":
#             splited_numbers.append(int(string1))
#             string1 = ""
#         else:
#             string1 += i
    
#     max = splited_numbers[0]
#     min = splited_numbers[0]
    
#     for x in splited_numbers[1:]:
#         if max < x:
#             max = x
#         if min > x:
#             min = x
#     return str(max) + " " + str(min)



# def find_short(s):
#     splited_str = s.split()
    
#     min_len = len(splited_str[0])
    
#     for i in splited_str[1:]:
#         if len(i) < min_len:
#             min_len = len(i)
#      return min_len