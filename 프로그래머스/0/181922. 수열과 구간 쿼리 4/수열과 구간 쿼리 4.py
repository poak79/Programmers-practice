def solution(arr, quer):
    for s, e, k in quer:
        for j in range(s, e+1):
            if j%k == 0:
                arr[j] += 1
    return arr