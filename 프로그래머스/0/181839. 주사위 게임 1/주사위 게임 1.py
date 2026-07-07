def solution(a, b):
    res = 0
    if a%2!=0 and b%2!=0:
        res += (a**2+b**2)
    elif a%2!=0 or b%2!=0:
        res += 2*(a+b)
    else:
        res += abs(a-b)
        
    return res