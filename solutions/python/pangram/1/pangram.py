def is_pangram(sentence):
    res = {c.lower() for c in sentence if c.isalpha()}

    return len(res) == 26