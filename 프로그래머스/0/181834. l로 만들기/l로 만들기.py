def solution(myString):
    res = ''
    for i in myString:
        if i<'l':
            res += 'l'
        else:
            res += i
            
    return res