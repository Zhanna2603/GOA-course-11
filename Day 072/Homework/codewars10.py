"""https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python"""

# Dashatize it

def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')