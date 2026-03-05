def bubble_sort(arr):
    if not isinstance(arr,list):
        raise TypeError("input must be a list")
    n=len(arr)
    for i in range(n):
        swap=False
        for d in range(0,n-i-1):
            if arr[d]>arr[d+1]:
                arr[d],arr[d+1]=arr[d+1],arr[d]
                swap=True
        if not swap:
            break
    return arr

numbers=[5,3,8,4]
print(bubble_sort(numbers))