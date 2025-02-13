"""Ask user for five names (use input five times). Add all of them in one list and print only first three names."""

names = []

for i in range(1, 6):
    name = input(f"Enter name {i}:")
    names.append(name)
print("The 1-st three names are:", names[:3])
