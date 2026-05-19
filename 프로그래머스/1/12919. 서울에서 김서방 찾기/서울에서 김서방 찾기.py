def solution(seoul):
    idx = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            idx = i
    return (f"김서방은 {idx}에 있다")
            