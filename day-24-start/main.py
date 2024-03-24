# Reading files
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# Absolute file path
# with open("/Users/Nadja/OneDrive - University of Illinois - Urbana/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Relative file path
with open("../../OneDrive - University of Illinois - Urbana/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


# Writing to files
# # my_file.txt is read-only, so need to use mode option to write to it
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# if you don't want to overwrite the contents of the file, use "a" to append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# can also use write() to create a new file
# a new file will be opened if no file with that name already exists
with open("new_file.txt", mode="w") as file:
    file.write("New file text.")
