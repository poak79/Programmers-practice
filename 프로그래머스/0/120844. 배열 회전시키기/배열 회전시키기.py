def solution(num, direc):
    if direc == "right":
        return num[-1:] + num[:-1]
    elif direc == "left":
        return num[1:] + num[0:1]