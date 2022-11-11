def find_longest_length(s):
    checklist = {}
    start = 0
    lon_len = 0
    if s == '':
        return s 
    for i, v in enumerate(s):
        if v in checklist:
            start = max(start, checklist[v] + 1)
        if v in checklist:
            result = s[checklist[v]:i]
        checklist[v] = i
        lon_len = max(lon_len, i - start + 1)
    return result, lon_len
    

## Main
phrase = 'aabcaadaefa'
find_longest_length(phrase)