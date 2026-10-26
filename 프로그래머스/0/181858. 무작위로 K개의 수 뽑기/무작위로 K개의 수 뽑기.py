def solution(arr, k):
    res = list(dict.fromkeys(arr))[:k]
    return res + [-1] * (k - len(res))
    