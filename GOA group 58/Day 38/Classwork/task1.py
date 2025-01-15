def reverse_words(string1):
    splited_str = string1.split()

    return " ".join(splited_str[::-1])

print(reverse_words("Hello World"))
print(reverse_words("Python is great"))
print(reverse_words("a b c"))
print(reverse_words(""))
print(reverse_words(" Spaces " ))




def check_exam(arr1,arr2):
    score = 0
    
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
    if score < 0:
        return 0
    return score