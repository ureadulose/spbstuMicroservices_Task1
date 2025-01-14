import re

def process(raw_str):
    res = True

    str = re.sub(r'[^a-zA-Z0-9а-яА-Я]', '', raw_str) # the rule "removes" all the other symbols except the letters and digits

    if (len(str) == 0):
        res = False
        return res

    str_rev = str[::-1]

    for sym, sym_rev in zip(str, str_rev):
        if sym != sym_rev:
            res = False
            break
    
    return res

def palindrome_check(str):
    if (process(str)):
        print(f'"{str}" is a palindrome!')
    else:
        print(f'"{str}" is not a palindrome!')

if __name__ == '__main__':
    palindrome_check("palindrome")
    palindrome_check("фыввы ф")
    palindrome_check("дед")
    palindrome_check(" turtle eltrut")