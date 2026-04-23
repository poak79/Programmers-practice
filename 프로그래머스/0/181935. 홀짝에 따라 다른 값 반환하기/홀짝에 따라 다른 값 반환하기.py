def solution(n):
    res = 0
    if n%2 != 0:
        for i in range(1, n+1):
            if i%2 != 0:
                res += i
        return res
    else:
        for i in range(1, n+1):
            if i%2 == 0:
                res += i*i
        return res
                