def bubble_sort_right_left(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for d in range(n-1,i,-1):
            if arr[d]>arr[d-1]:
                arr[d],arr[d-1]=arr[d-1],arr[d]
                swap=True
        if not swap:
            break
    return arr

numbers=[5,3,8,4]
print(bubble_sort_right_left(numbers))
