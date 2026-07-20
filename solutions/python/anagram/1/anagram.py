def find_anagrams(word, candidates):
    
    word_sorted = sorted(word.lower())
    res = [cand for cand in candidates if (sorted(cand.lower()) == word_sorted) and (cand.lower() != word.lower())]

    return res

    
 


