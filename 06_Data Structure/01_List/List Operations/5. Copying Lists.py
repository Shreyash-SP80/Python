original = [1, [2, 3]]
shallow = original.copy()  # or list(original)
 
print(shallow)        # [1, [2, 3]]

# Modify nested list in shallow copy
shallow[1][0] = 99

print(original)  # [1, [99, 3]]  ← Original CHANGED!
print(shallow)   # [1, [99, 3]]

import copy

original = [1, [2, 3]]
deep = copy.deepcopy(original)

# Modify nested list in deep copy
deep[1][0] = 99

print(original)  # [1, [2, 3]]  ← Original UNCHANGED
print(deep)      # [1, [99, 3]]