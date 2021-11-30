import plotly.express as px 
import pandas as pd 
import csv

with open("csv/cups of coffee vs hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Sleep", y = "Coffee")
    fig.show()