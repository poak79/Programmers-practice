def solution(cipher, code):
    res = ''
    for i in range(len(cipher)):
        if (i+1)%code == 0:
            res += cipher[i]
            
    return res