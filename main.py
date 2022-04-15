"""
    Learn Data Structure amd Data Analysis in Python With Pandas

    https://pandas.pydata.org/docs/reference/index.html
    https://pandas.pydata.org/docs/
"""

# 1. Open weather_data.csv and create a list a named data that contains the value from it ( normal file )
with open("weather_data.csv") as file_weather:
    weather_list = file_weather.readlines()
    print(weather_list)

# 2. Open weather_data.csv and create a list a named data that contains the value from it ( csv file )
import csv
with open("weather_data.csv") as file_weather:
    weather_list = csv.reader(file_weather)
    for row in weather_list:
        print(row)

# 3. Extract temperature from csv file
with open("weather_data.csv") as file_weather:
    temperature = []
    weather_list = csv.reader(file_weather)
    for row in weather_list:
        if row[1] != 'temp':
            temperature += [int(row[1])]
    print(temperature)

# 4. Utilize pandas module https://pandas.pydata.org/docs/ data structure and data analysis tool
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

# 5. Extract temperature from csv file
print(data["temp"])

# 6. Data Structure in Pandas = Series and DataFrame
#    DataFrame equivalent with whole table in csv, or a table in one excel sheet tab
print(type(data))
#    Series equivalent to a single list or single column in excel
print(type(data["temp"]))

# 7. Convert csv data (Series)  to Dictionary
data_dict = data.to_dict()
print(data_dict)
#   Convert temp column (DataFrame) to a List
temp_list = data["temp"].to_list()
print(temp_list)

# 8. Get average of temperature from Column temp
average_temp = sum(temp_list)/len(temp_list)
print(f"average temperature in csv file is {average_temp}")
average_temp2 = data["temp"].mean()
print(f"average temperature in csv file is {average_temp2}")
max_temp = data.temp.max() # equivalent with data["temp"].max()
print(f"max temperature in csv file is {max_temp}")

# 9. Get weather condition
weather_condition = data.condition # equivalent with data["condition"]
print(f"weather condition {weather_condition.to_list()}")

# 10. Filter data on monday
data_on_monday = data[data.day == "Monday"]
print( data_on_monday )
temp_on_monday = data_on_monday.temp
print(f"temperature on Monday is {temp_on_monday.values} Celcius ")


# 11. Find data which had the highest temperature
highest_temp_data = data[ data.temp == data.temp.max() ]
print(highest_temp_data)
print(highest_temp_data.condition.values[0])

# 12. Convert Monday temperature to Fahrenheit
temp_on_monday = data[data.day == "Monday"].temp.values[0]
fahrenheit_temp_on_monday = temp_on_monday * 1.8 + 32
print(f"temperature on Monday is {fahrenheit_temp_on_monday} Fahrenheit ")

# 13. Create data frame from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data_dict)

# 14. Generate to Csv File
data.to_csv("new_data.csv")





