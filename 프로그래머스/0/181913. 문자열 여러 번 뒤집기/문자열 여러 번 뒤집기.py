def solution(my, quer):
    for s, e in quer:
        my = my[:s] + my[s:e+1][::-1] + my[e+1:]
    return my
                 