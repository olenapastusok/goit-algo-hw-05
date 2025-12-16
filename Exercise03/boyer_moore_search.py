def build_shift_table(pattern):
    shift_table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        shift_table[char] = length - index - 1
    
    shift_table.setdefault(pattern[-1], length)

    return shift_table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        
        if j < 0 :
            return i  # Pattern found at index i
        
        else:
            i += shift_table.get(text[i + m - 1], m)
    return -1  # Pattern not found