def solution(my, pre):
    for i in range(1, len(my)):
        if pre == my[0:i]:
            return 1
        
    return 0