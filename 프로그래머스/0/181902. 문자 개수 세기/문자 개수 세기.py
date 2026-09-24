def solution(my):
    up = [0] * 26
    low = [0] * 26
    for c in my:
        if 'A' <= c <= 'Z':
            up[ord(c) - ord('A')] += 1
        elif 'a' <= c <= 'z':
            low[ord(c) - ord('a')] += 1
            
    return up + low