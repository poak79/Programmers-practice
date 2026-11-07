def solution(arr, divisor):
    res = []
    for i in arr:
        if i % divisor == 0:
            res.append(i)
    if res:
        res.sort()
        return res
    else:
        res.append(-1)
        return res