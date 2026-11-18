def solution(rank, attendance):
    s = sorted([i for i in range(len(rank)) if attendance[i]], key=lambda i: rank[i])
    a, b, c = s[:3]
    return 10000 * a + 100 * b + c