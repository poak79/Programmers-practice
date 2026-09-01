def solution(num):
    num.sort()
    return max(num[0]*num[1], num[-1]*num[-2])