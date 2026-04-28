def solution(num):
    even = ''
    odd = ''
    for s in num:
        if s % 2 == 0:
            even += str(s)
        else:
            odd += str(s)
    return int(even) + int(odd)