def solution(arr):
    s = set(arr)
    counts = [arr.count(i) for i in s]
    m = max(counts)
    if counts.count(m) > 1:
        return -1
    return max(s, key=arr.count)
    