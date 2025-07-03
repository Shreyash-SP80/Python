# Similar to switch-case in other languages
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not found")  # This will execute
    case _:  # Default case
        print("Unknown status")