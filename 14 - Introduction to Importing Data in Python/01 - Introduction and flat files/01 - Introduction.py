def read_file(file_name):
    # Open the file in read mode using a context manager
    with open(file_name, mode='r') as file:
        # Read and print the entire content of the file
        file_contents = file.read()
        print("File Contents:\n", file_contents)

    # Check whether the file is closed after exiting the context
    print("File Closed:", file.closed)

    # Open the file again using a context manager
    with open(file_name) as file:
        # Read and print the first 3 lines
        for _ in range(3):
            line = file.readline()
            if line:
                print("Line:", line.strip())
            else:
                print("Reached end of file.")

    # Check whether the file is closed after exiting the context
    print("File Closed:", file.closed)

# Call the function with the file name
file_name = '../data/moby_dick.txt'
read_file(file_name)