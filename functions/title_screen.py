def display_title_screen():
    # Open the .txt file for reading
    file_path = 'resources/title_screen.txt'
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file
            title_screen = file.read()
            # Print the contents to the console
            print(title_screen)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Leave Title Screen
    return title_screen