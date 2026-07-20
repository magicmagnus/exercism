def is_armstrong_number(number):
    str_number = str(number)

    digits = len(str_number)

    res = 0 
    for digit in str_number:
        res += int(digit) ** digits

    return res == number