import pandas as pd

data = pd.read_csv("../sources/2018_Central_Park_Squirrel_data.csv")

color_section = data["Primary Fur Color"]

black_color = len(data[color_section == "Black"])
gray_color = len(data[color_section == "Gray"])
cinnamon_color = len(data[color_section == "Cinnamon"])

data_dict = {
    "Fur Color" : ["Black", "Gray", "Cinnemon"],
    "Count" : [black_color, gray_color, cinnamon_color]
}

df = pd.DataFrame(data_dict)
print(df)

#Create new csv file
# df.to_csv("new_file_name")
