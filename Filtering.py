import pandas as pd
from icecream import ic

df = pd.read_csv("World Largest Cities by Population 2024.csv")

# p1 -- find cities population greater than 20 million

p1 = df[ df['Population (2024)'] > 20000000 ]
ic(p1)

# p2 -- find all largest cities in vietnam

p2 = df [ df["Country"] == "Vietnam"]

#p3 - find Cities in china that are growing in population in 2024 (+ve growth)

p3 = df[ (df["Country"] == "China") & (df["Growth Rate"] > 0)] 

#p4 claculate the total population in india

cities_india = df [ df["Country"] == "India"].sum()
ic(int(cities_india["Population (2024)"]))

#p5 calculate the cities expericning the a population decline and calculate their growth median
decline_cities = df [ df["Growth Rate"] < 0]
p5 = decline_cities["Population (2024)"].median()
ic(int(p5))

#p6 find the growing cities in china ad=nd find the minimum population they had in 2023

p6 = df [(df["Country"] == "China") & (df["Growth Rate"] > 0)]
ic(p6["Population (2023)"].min())