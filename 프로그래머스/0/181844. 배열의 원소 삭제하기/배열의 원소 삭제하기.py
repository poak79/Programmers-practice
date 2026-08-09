def solution(arr, delete):
    res = []
    for i in arr:
        if i in delete:
            continue
        else:
            res.append(i)
    
    return res
        