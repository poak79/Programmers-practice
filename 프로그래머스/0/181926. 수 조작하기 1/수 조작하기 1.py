def solution(n, con):
    cont = list(con)
    for s in cont:
        if s == "w":
            n += 1
        elif s == "s":
            n -= 1
        elif s == "d":
            n += 10
        elif s == "a":
            n -= 10
        
    return n
    