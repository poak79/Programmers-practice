def solution(arr, queries):
    res = []
    for s, e, k in queries:
        can = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        res.append(min(can) if can else -1)
        
    return res