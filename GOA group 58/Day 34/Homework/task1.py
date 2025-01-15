"""1) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.

არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება"""

def manual_replace(s):
    new_string = ""
    for i in s:
        if i == " ":
            new_string += "-"
        else:
            new_string += i
    return new_string