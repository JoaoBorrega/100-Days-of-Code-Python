# 🚨 using just file methods

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# 🚨 using csv library

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

# 🚨

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 🚨 using pandas library

import pandas

data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

print("\n")

temp_list = data["temp"].to_list()
print(temp_list)

print("\n")

# average = sum(temp_list) / len(temp_list)
# print(average)
print(data["temp"].mean())

print("\n")

print(data["temp"].max())

print("\n")

# 🚨 get Data in columns

print(data["condition"])
# ou
print(data.condition)

print("\n")
# 🚨 get data in row

print(data[data.day == "Monday"])

print("\n")

print(data[data.temp == data.temp.max()])

print("\n")

monday = data[data.day == "Monday"]
print(monday.condition)

print("\n")

# 🚨 get row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

print("\n")
# 🚨 create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

