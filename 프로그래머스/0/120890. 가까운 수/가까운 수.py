def solution(arr, n):
    best = arr[0]
    for i in arr:
        d = abs(i - n)
        bd = abs(best - n)
        if d < bd or (d == bd and i < best):
            best = i
    
    return best