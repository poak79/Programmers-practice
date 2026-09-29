def solution(my):
    arr = my.split()
    ans = int(arr[0])
    
    for i in range(1, len(arr), 2):
        if arr[i] == "+":
            ans += int(arr[i+1])
        else:
            ans -= int(arr[i+1])
            
    return ans