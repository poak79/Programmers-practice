def solution(my, is_suffix):
    for i in range(0, len(my)):
        if is_suffix == my[i:]:
            return 1
            
    return 0