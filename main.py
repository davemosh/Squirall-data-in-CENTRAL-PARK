#with open("weather_data.csv.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
# import csv
# with open("weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     tempreture = []
#     for row in data:
#         if row[1] != "temp":
#             tempreture.append(row[1])
#     print(tempreture)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241106.csv")
grey_squarrial = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squarrial = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squarrial = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squarrial)
print(cinnamon_squarrial)
print(black_squarrial)

data_data = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [grey_squarrial, cinnamon_squarrial, black_squarrial]
}

df = pandas.DataFrame(data_data)
df.to_csv("Squirrel_count.csv")


















    