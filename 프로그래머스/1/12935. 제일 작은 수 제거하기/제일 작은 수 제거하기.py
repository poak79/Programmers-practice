def solution(arr):
    res = []
    if len(arr) == 1:
        res.append(-1)
    else:
        arr.remove(min(arr))
        res = arr
    
    return res