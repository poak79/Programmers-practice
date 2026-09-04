def solution(age):
    al = "abcdefghij"
    return ''.join(al[int(d)] for d in str(age))