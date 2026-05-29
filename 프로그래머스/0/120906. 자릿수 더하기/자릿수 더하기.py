def solution(n):
    res = 0
    for i in range(len(str(n))):
        res += n%10
        n //= 10        
        
    return res