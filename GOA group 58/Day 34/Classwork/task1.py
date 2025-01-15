# list = [1, 2, 3, 4]
# for item in list:
#     if item == 1:
#         print (item)

# # list() არის ფუნქცია, რომელსაც არგუმენტად შეიძლება გადეცეს string-ი და ის გადააქცევს მას სიად

# string = input("Enter a string")
# x = 0
# for i in string:
#     print(i+"-"+(x))
#     x +=1



# #     2) შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი

# # არ გამოიყენოთ .join() ფუნქცია

# def manual_join(str_list, divider):
#     if not str_list:
#         return ""
#     result = str_list[0]
#     for string in str_list[0:]:
#         result+=divider + string
#     return result


# Аналог:
#     def manual_join(str_list, string1):
#     result = ""

#     for i in str_list:
#         result += i + string1
#     return result[:-3]


# print(manual_join(list("Python"), " - "))


# 3) შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ნა სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.

# 4) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.
#  არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება

# 5) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.

# გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step

# 3)

def manual_count(nums_list, number):
    count = 0
    for i in nums_list:
        if i == number:
            count += 1
    return count 

# 4)
def manual_replace(num):
# replaced " " to "-"
    # num = num.replace(" ","-")
    if num = " "
    # მე-0 სიის ელემენტიდან ვიყებ
    res = num[0]
    for i in range(1, len(num)):
        return res

