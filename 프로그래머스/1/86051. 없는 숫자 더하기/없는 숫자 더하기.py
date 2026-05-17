def solution(num):
    res = 0
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(len(arr)):
        if arr[i] not in num:
            res += arr[i]
            
    return res