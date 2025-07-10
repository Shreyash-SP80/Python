# Create a function that takes a list and a multiplier, then returns a new list where each element is multiplied by the given value.
# Example: multiply_list([1, 2, 3], 3) → [3, 6, 9]

def  list_Multiplier(arr, mul):
    yield arr * mul

list = [1, 2, 3]
mul = 3
list2 = []

for j in list:
   for i in list_Multiplier(j, mul):
       list2.append(i)
print(list2)   # [3, 6, 9]+