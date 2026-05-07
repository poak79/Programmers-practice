def solution(intStrs, k, s, l):
    answer = []
    for i in range(0, len(intStrs)):
        res = int(intStrs[i][s:s+l])
        if res > k:
            answer.append(res)
    
    return answer