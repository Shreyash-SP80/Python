# File Modes Demonstration Program

def demonstrate_r_plus_mode():
    """r+ mode: Read and write (file must exist)"""
    print("\n=== r+ Mode (Read/Write existing file) ===")

    try:
        with open("Modestext.txt", "r+", encoding="utf-8") as f:
            print("Initial content:", f.read())
            f.write("\nNew line added in r+ mode")
            f.seek(0)
            print("After writing:", f.read())
    except FileNotFoundError:
        print("File doesn't exist - create it first")

def demonstrate_w_plus_mode():
    """w+ mode: Write and read (truncates existing file or creates new)"""
    print("\n=== w+ Mode (Write/Read - truncates) ===")

    with open("Modestext.txt", "w+", encoding="utf-8") as f:
        f.write("Initial content in w+ mode\n")
        f.seek(0)
        print("Content after writing:", f.read())

def demonstrate_a_plus_mode():
    """a+ mode: Append and read (creates file if doesn't exist)"""
    print("\n=== a+ Mode (Append/Read) ===")

    with open("Modestext.txt", "a+", encoding="utf-8") as f:
        f.write("New line added in a+ mode\n")
        f.seek(0)
        print("All content:", f.read())

def demonstrate_x_mode():
    """x mode: Exclusive creation (fails if file exists)"""
    print("\n=== x Mode (Exclusive creation) ===")

    try:
        with open("Modestext1.txt", "x", encoding="utf-8") as f:
            f.write("Created new file with x mode\n")
            print("File created successfully")
    except FileExistsError:
        print("File already exists - can't use x mode")

def demonstrate_x_plus_mode():
    """x+ mode: Exclusive creation with read/write"""
    print("\n=== x+ Mode (Exclusive read/write) ===")

    try:
        with open("2.txt", "x+", encoding="utf-8") as f:
            f.write("Initial content in x+ mode\n")
            f.seek(0)
            print("Content:", f.read())
    except FileExistsError:
        print("File already exists - can't use x+ mode")

def create_initial_files():
    """Create initial files for demonstration"""
    with open("Modestext.txt", "w", encoding="utf-8") as f:
        f.write("Existing content\n")
    with open("Modestext.txt", "w", encoding="utf-8") as f:
        f.write("Existing content\n")

def main():
    # Setup initial files
    create_initial_files()
    
    # Demonstrate each mode
    demonstrate_r_plus_mode()
    demonstrate_w_plus_mode()
    demonstrate_a_plus_mode()
    demonstrate_x_mode()
    demonstrate_x_plus_mode()

if __name__ == "__main__":
    main()