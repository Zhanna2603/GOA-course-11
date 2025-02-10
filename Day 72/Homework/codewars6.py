"""https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python"""

# Help the bookseller !

def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    
    category_sums = {}
    for entry in stocklist:
        code, quantity = entry.split()
        category = code[0]
        q = int(quantity)
        category_sums[category] = category_sums.get(category, 0) + q
    
    result = []
    for cat in categories:
        total = category_sums.get(cat, 0)
        result.append(f"({cat} : {total})")
    
    return " - ".join(result)