import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

color_count_gray =(data["Primary Fur Color"]=="Gray").sum()
color_count_red =(data["Primary Fur Color"]=="Cinnamon").sum()
color_count_black =(data["Primary Fur Color"]=="Black").sum()

new_csv_data= {
    "Fur Color":["Gray","Red","Black"],
    "Count":[color_count_gray,color_count_red,color_count_black],
}

new_data = pd.DataFrame(new_csv_data)
new_data.to_csv("new_csv.csv",index=False)

