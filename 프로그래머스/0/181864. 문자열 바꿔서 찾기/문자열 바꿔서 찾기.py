def solution(my, pat):
    tmp = ''
    for i in my:
        if i == 'A':
            tmp += 'B'
        else:
            tmp += 'A'
            
    if pat in tmp:
        return 1
    else:
        return 0