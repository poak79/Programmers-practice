def solution(arr, inter):
    res = []
    for i, j in inter:
        for s in range(i, j+1):
            res.append(arr[s])
            
    return res
    