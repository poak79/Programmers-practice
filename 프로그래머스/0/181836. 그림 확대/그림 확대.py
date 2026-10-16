def solution(picture, k):
    return [''.join(c * k for c in s) for s in picture for _ in range(k)]