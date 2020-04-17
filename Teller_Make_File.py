##
##Code Tester - Get Input and Write to File
##

num = input("Enter the number of people you wish to register: ")

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def append_text(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:

        # Append text at the end of file
        file_object.write(text_to_append)

for i in range(int(num)):
    name = input("Enter your name: ")
    languages = input("Enter the languages you speak: ")
    services = input("Enter the services you can perform: ")
    location = input("Enter your location by country code: ")
    availability = input("Are you available for services (0 or 1)? ")
    append_new_line('People.txt', name + ', ')
    append_text('People.txt', 'language, ' + languages + ', ')
    append_text('People.txt', 'service, ' + services + ', ')
    append_text('People.txt', 'location, ' + location + ', ')
    append_text('People.txt', 'availability, ' + availability)

