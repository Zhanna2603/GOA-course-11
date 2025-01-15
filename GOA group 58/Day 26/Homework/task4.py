"""4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას"""

def replace(text):
    word_list = text.split(" ")
    dashed_text = "-".join(word_list)
    return dashed_text