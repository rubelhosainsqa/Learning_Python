
# Put the files location and need to input double forward slash in the location path
file = open("C:\\Users\\Rubel\\Documents\\Automation_Testing\\Files\\test.xlsx","w")
# Write to the file
file.write("I am Rube Hosain.\n")
file.write("I am SQA Engineer")
file.close()

# Read from file
file = open("C:\\Users\\Rubel\\Documents\\Automation_Testing\\Files\\test.xlsx","r")
print(file.read())
file.close()
