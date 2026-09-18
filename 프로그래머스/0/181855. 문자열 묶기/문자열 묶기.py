from collections import Counter

def solution(Arr):
    cnt = Counter(len(s) for s in Arr)
    return max(cnt.values())