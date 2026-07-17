def solution(arr, flag):
    res = []
    for i in range(0, len(arr)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                res.append(arr[i])
        elif flag[i] == False:
            for j in range(arr[i]):
                res.pop()
                
    return res