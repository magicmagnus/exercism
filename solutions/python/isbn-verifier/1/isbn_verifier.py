def is_valid(isbn):
    cleaned = isbn.strip().replace('-', '')

    digits = '0123456789'

    res = []
    if len(cleaned) != 10:
        return False
        
    for i, el in enumerate(cleaned):
        if el in digits:
            res.append(int(el))
        elif el == 'X' and i == 9:
            res.append(10)
        else:
            return False
            
    

    summe = sum([res[i] * (10 - i) for i in range(10)])

    return summe % 11 == 0