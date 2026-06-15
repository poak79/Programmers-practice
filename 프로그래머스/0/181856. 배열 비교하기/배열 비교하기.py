def solution(arr1, arr2):
    res1 = 0
    res2 = 0
    if len(arr1) > len(arr2):
        return(1)
    elif len(arr2) > len(arr1):
        return(-1)
    elif len(arr1) == len(arr2):
        for i in arr1:
            res1 += i
        for i in arr2:
            res2 += i
        if res1 > res2:
            return(1)
        elif res2 > res1:
            return(-1)
        elif res1 == res2:
            return(0)