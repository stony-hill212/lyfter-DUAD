All={1,2,3,4,5,6,7,8,9,10}
Even={2,4,6,8,10}
Odd={1,3,5,7,9}

union_result=Even | Odd
print("1. Even u Odd:", union_result)

intersection_result=Even & Odd
print("2. Even n Odd", intersection_result)

difference_result=All | Odd
print("3. All - Odd:", difference_result)

complement_even=All - Even
print("4. C(Even):", complement_even)

temp=Odd - All
print("Step A (Odd - All):", temp)

complement_result=All - temp
print("5. C(Odd - All):", complement_result)

