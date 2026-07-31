def solution(my):
    res = ''
    for i in my:
        if i.islower():
            res += i.upper()
        elif i.isupper():
            res += i.lower()
    return res