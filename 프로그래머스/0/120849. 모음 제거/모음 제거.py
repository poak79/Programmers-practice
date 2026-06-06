def solution(my):
    res = ""
    for i in my:
        if i not in "aeiou":
            res += i
            
    return res
    