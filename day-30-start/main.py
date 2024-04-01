# FileNotFoundError
# with open("a_file.text") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# # Have to specify which error you want the exception to address
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# # Else block is only executed if no exceptions were found
# else:
#     content = file.read()
#     print(content)
# # Finally block runs no matter what happens
# finally:
#     raise KeyError("This is an error I made up")
#     # file.close()
#     # print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Human height should not exceed 3 meters.")

bmi = weight / height ** 2
print(bmi)
