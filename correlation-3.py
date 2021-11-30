import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
    marks = []
    days = []

    with open("csv/Student Marks vs Days Present.csv") as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return{
        "x" : marks,
        "y" : days
    }


def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("Correlation betweem marks and days present: \n", correlation[0,1])

def  plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
        fig.show()


def setUp():
    data_path = "csv/Student Marks vs Days Present.csv"

    data_source = getDataSource(data_path)
    find_correlation(data_source)
    plotFigure(data_path)
    
setUp()