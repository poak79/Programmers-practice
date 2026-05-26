def solution(arr):
    maxs = max(arr)
    idx = arr.index(maxs)
    return [maxs, idx]