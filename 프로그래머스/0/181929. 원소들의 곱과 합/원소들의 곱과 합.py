def solution(num):
    mult = 1
    for s in num:
        mult *= s
        
    mults = sum(num)**2
    
    if mult < mults: 
        return 1 
    else: 
        return 0
    