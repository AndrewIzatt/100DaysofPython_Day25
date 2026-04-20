from turtledemo.nim import COLOR

import pandas
# data = pandas.read_csv("./weather_data.csv")
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(len(temp_list))
# print(temp_list)
# print(avg_temp)
#
# average = data["temp"].mean()
# print(average)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data[data.temp == data.temp.max()])

# ************ Squirrel Census **************
data = pandas.read_csv("./2018_squirrel_census.csv")

# fur_colors = data.groupby("Primary Fur Color").size()
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

df = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(df)
df.to_csv("squirrel_counts.csv")
# df.to_csv("squirrel_counts.csv")
# print(data_frame)
# print(data_frame)
# gray_squirrels = data_frame["Primary Fur Color"] == "Gray"
# print(gray_squirrels)
# print(type(fur_colors))
# print(fur_colors)
# fur_colors.to_csv("./squirrel_counts.csv")
# print(fur_colors_size[0])
# print(fur_colors.size())
# print(fur_colors)
# print(fur_colors[0])

# data_dict = {
#     "Fur Color" : ["grey", "red", "black"]
# }