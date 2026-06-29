def solution(myString):
    res = ""
    for i in myString:
        if i == 'a':
            res += i.upper()
        elif i == 'A':
            res += i
        else:
            res += i.lower()
    
    return res