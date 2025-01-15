"""7) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ"""

list1 = [5, 2, 3]
list2 = [7, 9, 1]

def multiply_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return (sum1 * sum2)

result = multiply_sums(list1, list2)
print(result)
