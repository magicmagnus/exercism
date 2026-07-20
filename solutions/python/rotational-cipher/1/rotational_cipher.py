def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for c in text:
        if c.isalpha():
            index = (alphabet.index(c.lower()) + key) % 26
            c = alphabet[index] if c.islower() else alphabet[index].upper()
        res += c 
    return res
