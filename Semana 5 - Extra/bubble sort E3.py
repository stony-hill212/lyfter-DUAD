def validate_bubble_sort(arr):
    if not arr:
        print("Error: list cannot be empty.")
        return
    for item in arr:
        if not isinstance(item,(int,float)):
            print("Error: only numbers allowed")
            return
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
        print("Sorted list:", arr)

validate_bubble_sort([8,"MMA",10])
validate_bubble_sort([])
validate_bubble_sort([5,3,8,2])