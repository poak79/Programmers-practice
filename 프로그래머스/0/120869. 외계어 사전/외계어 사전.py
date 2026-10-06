def solution(spell, dic):
    for c in dic:
        if sorted(c) == sorted(spell):
            return 1
    return 2