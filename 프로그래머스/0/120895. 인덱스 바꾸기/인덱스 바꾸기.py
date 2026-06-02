def solution(my, num1, num2):
    arr = list(my)
    arr[num1], arr[num2] = arr[num2], arr[num1]
    return ''.join(arr)