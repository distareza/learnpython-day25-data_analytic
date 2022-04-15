"""
    Squirrel in NYC on 2018 Data Census Analysis
    https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

    Challenges
    Create Csv file that contains squirrel fur color and count them

    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
"""
import pandas

# get data series from csv file
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# get available fur color
squirrel_fur_color = squirrel_data["Primary Fur Color"].unique()
print(squirrel_fur_color)

# colors = []
# counts = []
squirrel_map = {}
for color in squirrel_fur_color.tolist():
    if pandas.isna(color):
        continue
    count = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
    squirrel_map[color] = count

print(squirrel_map)

squirrel_dict = {
     "Fur color": squirrel_map.keys(),
     "Count": squirrel_map.values()
 }
print(squirrel_dict)

pandas.DataFrame(squirrel_dict).to_csv("new_squirrel_data_count.csv")


# # count the squirrel based on fur color
# group_data = squirrel_data.groupby(['Primary Fur Color']).count()
# print(group_data)
# group_data.to_csv("new_squirrel_data_count.csv")


