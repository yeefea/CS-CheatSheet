def my_atoi(str):
    s = str.strip(' ')
    is_positive = True
    if s.startswith('+'):
        is_positive = True
        s = s[1:]
    elif s.startswith('-'):
        is_positive = False
        s = s[1:]

    ascii_0 = ord('0')
    n = 0
    for char in s:
        if char >= '0' and char <= '9':
            n = n * 10 + (ord(char) - ascii_0)
        else:
            break
    if not is_positive:
        n = -n
    if n > 2147483647:
        n = 2147483647
    elif n < -2147483648:
        n = -2147483648
    return n


if __name__ == '__main__':
    print(my_atoi('3.14'))
