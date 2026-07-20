def is_isogram(phrase):
    res = set()
    for c in phrase.lower():
        if c in res:
            return False
        if c.isalpha():
            res.add(c)
    return True
