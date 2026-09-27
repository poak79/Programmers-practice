def solution(arr):
    res = 0
    for i in set(arr):
        cnt = 0
        while (i >= 50 and i % 2 == 0) or (i < 50 and i % 2 == 1):
            i = i // 2 if i >= 50 else i * 2 + 1
            cnt += 1
        res = max(res, cnt)
        
    return res