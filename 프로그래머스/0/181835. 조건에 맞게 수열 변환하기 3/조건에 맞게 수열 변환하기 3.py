def solution(arr, k):
    res = []
    if k%2==0:
        for i in arr:
            res.append(i+k)
    else:
        for i in arr:
            res.append(i*k)
    return res