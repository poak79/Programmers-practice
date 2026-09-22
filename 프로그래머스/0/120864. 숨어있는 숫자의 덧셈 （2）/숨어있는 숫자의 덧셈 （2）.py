def solution(my):
    for c in my:
        if not c.isdigit():
            my = my.replace(c, ' ')        
    return sum(int(x) for x in my.split())