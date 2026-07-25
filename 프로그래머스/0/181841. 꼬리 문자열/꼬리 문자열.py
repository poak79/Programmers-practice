def solution(str_list, ex):
    res = ''
    for i in str_list:
        if ex in i:
            continue
        else:
            res+=i
    return res