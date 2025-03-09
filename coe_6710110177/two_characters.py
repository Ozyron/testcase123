def is_alternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]: 
            return False
    return True

def alternate(s):
    unique_chars = list(set(s)) 
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            
            filtered_string = ''.join([c for c in s if c in (char1, char2)])

            if is_alternating(filtered_string):
                max_length = max(max_length, len(filtered_string))

    return max_length if max_length > 0 else 0