def solution(strli):
    for i in range(len(strli)):
        if strli[i] == 'l':
            return strli[:i]
        elif strli[i] == 'r':
            return strli[i+1:]
    
    return []