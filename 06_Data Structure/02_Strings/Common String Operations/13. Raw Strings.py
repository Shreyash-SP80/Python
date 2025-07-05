# Raw Strings:
# Raw strings are a special string format that treats backslashes (\) as literal characters rather than escape characters. 
# They are particularly useful when working with:
#   - Regular expressions
#   - Windows file paths
#   - Any strings containing many backslashes

# Syntax
#   r"string_content"  # lowercase r/
#   R"string_content"  # uppercase R (same meaning)

normal_str = "Hello\nWorld"  # \n becomes a newline
print(normal_str)
# Output:
# Hello
# World

raw_str = r"Hello\nWorld"  # \n remains as \n
print(raw_str)
# Output: Hello\nWorld


#  - Backslashes are treated literally - no escape sequences are processed
#  - Cannot end with an odd number of backslashes - the final quote would be escaped
#  - Identical to regular strings in all other ways