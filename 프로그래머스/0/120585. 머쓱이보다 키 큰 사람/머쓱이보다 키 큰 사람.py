def solution(arr, h):
    cnt = 0
    
    for i in range(len(arr)):
        if arr[i] > h:
            cnt += 1
            
    return cnt