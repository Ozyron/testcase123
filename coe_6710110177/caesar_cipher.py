def caesar_cipher(s, k):
    encrypted = []
    k = k % 26  
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
































