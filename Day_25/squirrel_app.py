import csv
import pandas

data = pandas.read_csv("squirrel_data.csv")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

black_squirrels_count = len(black_squirrels)
gray_squirrels_count = len(gray_squirrels)
cinnamon_squirrels_count = len(cinnamon_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")


