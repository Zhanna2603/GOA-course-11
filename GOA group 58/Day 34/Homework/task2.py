"""2) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.

გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step"""

def manual_range(start=0, stop=None, step=1):
    result = []
    if stop is None:
        stop = start
        start = 0
          
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        result.append(start)
        start += step
        
    return result 