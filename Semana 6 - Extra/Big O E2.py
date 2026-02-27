#1
def linear_search(my_list, target):  #O(n)
    for item in my_list:
        if item == target:
            return True
    return False

#2
def binary_search(my_list, target):  #(log n)
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#1. linear_search se podria utilizar si la lista no es muy grande,
#si la lista esta desordenada(unsorted), o si solo se necesita buscar una vez.

#2. binary_search se podria utilizar cuando es una lista grande/larga, cuando la lista esta ordenada(sorted)
#o si habira que buscar algo varias veces.

#3. Si my_list no esta ordenada(sorted),binary_search so rompe, 
#por lo tanto daria un resultado incorrecto.