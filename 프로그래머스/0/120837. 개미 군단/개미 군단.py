def solution(hp):
    res = 0
    
    res += hp // 5
    hp %= 5
    res += hp // 3
    hp %= 3
    res += hp // 1
    hp %= 1
    
    return res