def solution(my, pat):
    i = my.rfind(pat)
    return my[:i + len(pat)]