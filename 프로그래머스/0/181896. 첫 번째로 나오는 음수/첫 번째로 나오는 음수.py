def solution(num):
    for i in range(len(num)):
        if num[i]<0:
            return i
        
    return(-1)