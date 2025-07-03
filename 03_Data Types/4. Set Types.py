# 4. Set Types
# Unordered collections of unique items.

#    a) set
#     Mutable
#     No duplicate elements

unique_nums = {1, 2, 3, 2}  # {1, 2, 3}


#    b) frozenset
#     Immutable version of set

frozen = frozenset([1, 2, 3, 2])
print(frozen)    # frozenset({1, 2, 3})