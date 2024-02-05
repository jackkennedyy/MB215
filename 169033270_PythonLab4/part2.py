import traceback

# Writing to a file with exception handling
def write_to_file(sample, data):
    try:
        with open(sample, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {sample}")
        traceback.print_exc()

# Reading from a file
def read_from_file(sample):
    try:
        with open(sample, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the file: {sample}")
        traceback.print_exc()
        return None

# Appending to a file
def append_to_file(sample, data):
    try:
        with open(sample, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {sample}")
        traceback.print_exc()

# Demonstrating the functions
if __name__ == "__main__":
    # Writing to a file
    write_to_file('sample.txt', 'Hello, World!\n')
    
    # Reading from a file
    content = read_from_file('sample.txt')
    print("Content of 'sample.txt':")
    print(content)
    
    # Appending to a file
    append_to_file('sample.txt', 'This is an appended line.\n')

    # Reading again to show the appended content
    content = read_from_file('sample.txt')
    print("Updated content of 'sample.txt':")
    print(content)

    # Trying to read from a non-existent file to demonstrate exception handling
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")
