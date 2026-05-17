def solution(num):
    cnt = 0
    for i in range(len(num)):
        while num[i] != 1:
            if num[i]%2 == 0:
                num[i] /= 2
            else:
                num[i] = (num[i] - 1) / 2
            cnt += 1
            
    return cnt
            