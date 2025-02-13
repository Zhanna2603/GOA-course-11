"""https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python"""

# New Cashier Does Not Know About Space or Shift

def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    formatted_order = []
    
    for item in menu:
        lower_item = item.lower()
        count = order.count(lower_item)
        formatted_order.extend([item] * count)
        order = order.replace(lower_item, "")
    return " ".join(formatted_order)