def solution(my):
    for d in "abc":
        my = my.replace(d, " ")
        
    return my.split() or ["EMPTY"]