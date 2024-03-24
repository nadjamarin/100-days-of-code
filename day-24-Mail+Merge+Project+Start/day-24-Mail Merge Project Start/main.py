#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get list of names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

# Get starting letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    # print(letter)

# Replace [name] placeholder with actual name in the starting letter
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
    # Write the letter with replaced name to correct file name and location
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
    # print(new_letter)

