def solution(num, n):
    ans = []
    ans += num[n:]
    ans += num[:n]
    return ans