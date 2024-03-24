# # Read each line of the CSV into a list called data
# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# # Import CSV using local library
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)
#     # print(temperatures)



# Using pandas library
import pandas

# data = pandas.read_csv("weather_data.csv")
# Can print an entire column of data at once using the column title
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

# # Convert csv data to a dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # Can also convert to other data types
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Calculate average temperature
# # avg_temp = sum(temp_list)/len(temp_list)
# # pandas has built-in function to find avg of a column
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# # Find max temp
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Get data in columns
# # print(data["condition"])
# # Can also use this syntax: pandas adds column headers as attributes
# print(data.condition)  # case sensitive
#
# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)



# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# # Convert dictionary to a dataframe
# data = pandas.DataFrame(data_dict)
#
# # Export dataframe to CSV file
# new_data = data.to_csv("new_data.csv")



# Central Park squirrel census
# Goal: make CSV of squirrel colors and how many squirrels of each color
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240320.csv")
# fur_color_count = data["Primary Fur Color"].value_counts()
# fur_color_count.to_csv("squirrel_count.csv")
# # print(fur_color_count)

# Her solution
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
