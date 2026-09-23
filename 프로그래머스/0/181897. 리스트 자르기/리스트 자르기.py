def solution(n, slicer, num):
    a, b, c = slicer
    if n == 1:
        return num[:b+1]
    elif n == 2:
        return num[a:]
    elif n == 3:
        return num[a:b+1]
    elif n == 4:
        return num[a:b+1:c]