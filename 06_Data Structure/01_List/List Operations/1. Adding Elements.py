colors = ['red', 'green']

# Append (add to end)
colors.append('blue')      # ['red', 'green', 'blue']

# Adding element in list at perticular index position by removing old one
colors[1] = "pink"   
print(colors)          # ['red', 'pink', 'blue']

# Insert at specific position (index)
colors.insert(1, 'yellow') # ['red', 'yellow', 'green', 'blue']

# Extend (add multiple elements contining list)
colors.extend(['purple', 'orange']) # Adds two more colors

print(colors)  # ['red', 'yellow', 'green', 'blue', 'purple', 'orange']

# sort the list
colors.sort()
print(colors)     # ['blue', 'orange', 'pink', 'purple', 'red', 'yellow']