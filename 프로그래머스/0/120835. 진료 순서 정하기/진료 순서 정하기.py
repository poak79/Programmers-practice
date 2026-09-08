def solution(emergency):
    rank = sorted(emergency, reverse=True)
    return [rank.index(x) + 1 for x in emergency]