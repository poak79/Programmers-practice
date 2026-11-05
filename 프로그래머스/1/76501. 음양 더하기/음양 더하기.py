def solution(absolutes, signs):
    res = 0
    for i in range(0, len(absolutes)):
        if signs[i]:
            res += absolutes[i]
        else:
            res -= absolutes[i]
            
    return res