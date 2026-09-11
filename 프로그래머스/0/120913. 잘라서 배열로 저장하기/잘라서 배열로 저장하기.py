def solution(my, n):
    res = [my[i:i+n] for i in range(0, len(my), n)]
    return res