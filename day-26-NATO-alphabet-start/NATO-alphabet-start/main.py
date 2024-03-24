# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Get word from user
user_input = input("Enter a word: ").upper()
# Convert user's word into a list of letters
user_input_letters = [*user_input]

# Use NATO phonetic alphabet to get code for each letter in user's word
coded_letters = []
for i in user_input_letters:
    coded_letters.append(nato_dict[i])

# Print the coded letters to the screen for the user
print(coded_letters)
