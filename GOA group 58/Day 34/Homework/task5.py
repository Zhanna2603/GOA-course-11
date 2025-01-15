"""5) შექმენთ ფუნქცია, რომელიც არგუმენტად იღებს სიმბოლოების სიას. დაასორტირეთ ეს სია ანბანის მიხედვით, გადააქციეთ string-ად და დააბრუნეთ"""

def sort_and_convert_to_string(symbol_list):
    sorted_list = sorted(symbol_list)
    output_string = "".join(sorted_list)
    return output_string