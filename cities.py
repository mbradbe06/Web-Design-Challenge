#use pandas to read cities.csv into dataframe and then convert to html table for data.html page
import pandas as pd

cities_df = pd.read_csv("Resources/cities.csv")

cities_df.to_html('Resources/cities_table.html',index = False)
