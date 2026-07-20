def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for ch in text:
        if ch.isalpha():
            index = (alphabet.index(ch.lower()) + key) % 26
            c = alphabet[index] if ch.islower() else alphabet[index].upper()
        else:
            c = ch
        res += c 
    return res
