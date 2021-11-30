import plotly.express as px
import csv 
import numpy as np 

def getDataSource(data_path):
    temperature = []
    ice_cream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales"]))

    return {
        "x": temperature,
        "y": ice_cream_sales
    }


def find_correlation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation betweem VS Ice-cream Sales:\n", correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
        fig.show()


def setUp():
    data_path = "csv/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    dataSource = getDataSource(data_path)
    find_correlation(dataSource)
    plotFigure(data_path)

setUp()



