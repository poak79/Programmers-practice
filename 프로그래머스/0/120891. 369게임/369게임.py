def solution(order):
    cnt = 0
    for i in str(order):
        if i in "369":
            cnt += 1
    return cnt