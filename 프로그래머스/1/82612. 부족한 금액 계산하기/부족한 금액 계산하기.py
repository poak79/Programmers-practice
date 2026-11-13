def solution(price, money, count):
    use = 0
    for i in range(1, count+1):
        use += price*i
    
    return use - money if use > money else 0 