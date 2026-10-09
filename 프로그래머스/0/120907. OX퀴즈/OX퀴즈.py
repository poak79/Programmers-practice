def solution(quiz):
    answer = []
    for d in quiz:
        x, a, y, b, r = d.split()
        x, y, r = int(x), int(y), int(r)
        res = x + y if a == '+' else x - y
        answer.append("O" if res == r else "X")
        
    return answer