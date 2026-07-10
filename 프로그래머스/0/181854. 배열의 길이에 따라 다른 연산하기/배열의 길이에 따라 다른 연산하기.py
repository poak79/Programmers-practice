def solution(arr, n):
    for i in range(0, len(arr)):
        if len(arr)%2==0:
            if i%2!=0:
                arr[i] += n
        else:
            if i%2==0:
                arr[i] += n
    
    return arr
            