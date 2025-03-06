def staircase(n, pattern):
    result = ''
    for i in range(1, n + 1):
        result += pattern * i + '\n'
    return result
