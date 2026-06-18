def solution(num):
    odd = 0
    even = 0
    for i in range(0, len(num)):
        if i%2 != 0:
            odd += num[i]
        else:
            even += num[i]
            
    if odd > even:
        return odd
    else:
        return even
    
        
    