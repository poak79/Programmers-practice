def solution(bab):
    cnt = 0
    for d in bab:
        for s in ["aya", "ye", "woo", "ma"]:
            d = d.replace(s, " ")
        if d.strip() == "":
            cnt += 1
    return cnt