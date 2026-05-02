def solution(arr, quer):
    for i, j in quer:
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr