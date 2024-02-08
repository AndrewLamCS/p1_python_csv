def printCSV(file_path):
    """Prints out each row of a .csv file line by line
    
    Args:
        file_path (str): The path to the CSV file.

    Returns:
        None
    """
    try:
        # Attempt to open the file specified by file_path in read mode
        file = open(file_path, "r")     
        #Iterate over each line in the file
        for row in file:
            #Print each line
            print(file.readline())
    #If the specified file is not found, trigger FileNotFoundError
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

if __name__ == '__main__':
    # Prompt the user to enter the name of the CSV file
    file_name = input("Enter the name of the CSV file: ")

    # Call the function passing the provided file name
    printCSV(file_name)