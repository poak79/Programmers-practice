def solution(s):
    word = s.split(" ")
    res = []
    
    for c in word:
        words = ""
        for i in range(len(c)):
            if i%2==0:
                words += c[i].upper()
            else:
                words += c[i].lower()
        res.append(words)
        
    return ' '.join(res)