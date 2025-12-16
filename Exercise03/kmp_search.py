def create_lps(pattern):

    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):

    n = len(text)
    m = len(pattern)
    lps = create_lps(pattern)
    i = 0
    j = 0

    while i < n: 
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:   
            i += 1

        if j == m:
            return i - j  # Pattern found at index (i - j)
    return -1  # Pattern not found  