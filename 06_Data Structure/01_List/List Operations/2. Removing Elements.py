nums = [1, 2, 3, 4, 5, 6]

# Remove by value (Search specified element and remove)
nums.remove(3)           # Removes first occurrence of 3
print(nums)              #  [1, 2, 4, 5, 6]

# Remove by index
del nums[1]              # Removes element at index 1 (2)
print(nums)              # [1, 4, 5, 6]

popped = nums.pop(2)     # Removes and returns element at index 2 (5)
print(popped)            # 5

poped = nums.pop()       # Remove  an ending element
print(poped)             # 6

# Clear the list
nums.clear()             # Empties the list []
print(nums)              # []