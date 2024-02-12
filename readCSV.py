def printCSV(file_path):
    """Prints out each row of a .csv file line by line
    
    Args:
        file_path (str): The path to the CSV file.

    Returns:
        None
    """
    try:
        # Attempt to open the file specified by file_path in read mode
        #with statement includes __exit()__ method to close the file when operation is complete
        with open(file_path) as file:
            #Iterate over each line in the file
            for row in file:

                try:
                    #Splits row into a list of strings
                    splitted = row.split(',')

                    #Access first element of list - last name
                    lastname = splitted[0]

                    #Access second element of list - first name
                    firstname = splitted[1]

                    #Print each line as formatted string
                    print(f"Last Name: {lastname}, First Name: {firstname}")
                except IndexError:
                    print(f"Error: Row {row} is not in the correct format")

    #If the specified file is not found, trigger FileNotFoundError
    except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

if __name__ == '__main__':
    # Prompt the user to enter the name of the CSV file
    file_name = input("Enter the name of the CSV file: ")

    # Call the function passing the provided file name
    printCSV(file_name)