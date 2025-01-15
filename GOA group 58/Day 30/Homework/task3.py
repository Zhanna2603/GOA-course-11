"""3) შექმენით ფუნქცია manual_len, რომელსაც გადაეცემა სთრინგი ან სია, ხოლო ფუნქციამ უნდა დააბრუნოს გადმოცემული სთრინგის/სიის სიგრძე(არ გამოიყენოთ len-ი)
"""
def manual_len(obj):
    count = 0
    for item in obj:
        count += 1
    return count