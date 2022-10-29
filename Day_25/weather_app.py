import csv
import pandas
import statistics

#
# with open("weather_data.csv") as file:
#     weather_data_list = []
#
#     for row in csv.reader(file):
#         weather_data_list.append(row)
#     temperatures = []
#     for row in range(1, len(weather_data_list)):
#         temperatures.append(int(weather_data_list[row][1]))
#     print(temperatures)


data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].tolist()
row_with_highest_temp = data[data.day == "Monday"]
temp = row_with_highest_temp.temp
temp_in_celcius = row_with_highest_temp.temp * 1.8 + 32
print(temp_in_celcius)


list = [1,2,3,4,5,6]
num = 4
data = list[num]
