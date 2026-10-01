def solution(num, k):
    idx = 0
    for _ in range(k - 1):
        idx = (idx + 2) % len(num)
        
    return num[idx]