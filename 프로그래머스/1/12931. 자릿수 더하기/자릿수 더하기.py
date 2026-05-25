def solution(n):
    res = 0
    for _ in range(len(str(n))):
        res += n%10
        n = n//10
    return res
    