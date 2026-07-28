def solution(my_string):
    res = ''
    res += my_string.lower()
    res = ''.join(sorted(res))
    return res