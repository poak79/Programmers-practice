def solution(num, n):
    ans = 0
    for i in num:
        if ans <= n:
            ans += i
        else:
            break
    return ans