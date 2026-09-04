def solution(n):
    res = 0
    for i in range(1, n+1):
        div = 0
        for d in range(1, i+1):
            if i % d == 0:
                div += 1
        if div >= 3:
            res += 1
    return res