# def upper_and_lower(text):
#     upper_index = 1

#     result = ""

#     for i in text:
#         if upper_index == 3:
#             result += i.upper()
#             upper_index = 0
#         else:
#             result += i.lower()

#         upper_index += 1
#     return result


# print(upper_and_lower("HellO, MY namE IS Nika"))



def manual_capitalize(text):
     first_char = text[0].upper()
     other = text[1:].lower()
     return first_char + other
print(manual_capitalize(""))


def manual_capitalize(text):
     first_char = text[0].upper()
     other = text[1:].lower()
     return first_char + other
print(manual_capitalize(""))