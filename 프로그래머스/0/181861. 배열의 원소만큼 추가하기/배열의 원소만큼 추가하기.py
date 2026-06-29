def solution(arr):
    res = []
    for i in arr:
        res += [i] * i
    return res