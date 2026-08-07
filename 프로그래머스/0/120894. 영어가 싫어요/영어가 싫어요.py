def solution(num):
    res = num
    res = res.replace("one", "1")
    res = res.replace("two", "2")
    res = res.replace("three", "3")
    res = res.replace("four", "4")
    res = res.replace("five", "5")
    res = res.replace("six", "6")
    res = res.replace("seven", "7")
    res = res.replace("eight", "8")
    res = res.replace("nine", "9")
    res = res.replace("zero", "0")
    
    return int(res)