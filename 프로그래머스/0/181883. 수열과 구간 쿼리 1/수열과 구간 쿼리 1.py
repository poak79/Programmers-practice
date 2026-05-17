def solution(arr, quer):
    for s, e in quer:
        for i in range(s, e+1):
            arr[i] += 1
            
    return arr