def solution(num):
    res = num
    if res[len(res)-1] > res[len(res)-2]:
        res.append(res[len(res)-1] - res[len(res)-2])
        return res
    else:
        res.append(res[len(res)-1] * 2)
        return res