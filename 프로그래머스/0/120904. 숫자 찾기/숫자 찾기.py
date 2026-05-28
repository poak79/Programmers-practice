def solution(num, k):
    nums = []
    nums = str(num)
    for i in range(len(nums)):
        if nums[i] == str(k):
            return i + 1
        
    return -1
       