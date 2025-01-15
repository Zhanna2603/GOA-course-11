# 10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის
year = int(input("Enter a year:"))
century = year // 100 + 1
print(f"{century}")