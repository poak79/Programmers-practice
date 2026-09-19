def solution(num, n):
    return [num[i:i+n] for i in range(0, len(num), n)]