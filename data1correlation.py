import plotly.express as px
import csv 
import numpy as np
import pandas as pd

def getDataSource(datapath):
    iceCreamSales = []
    temperature = []
    with open(datapath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            temperature.append(float(i["Temperature"]))
            iceCreamSales.append(float(i["Ice-cream Sales"]))

    return {"x": temperature, "y": iceCreamSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Temperature and Ice-cream Sales is: ", correlation[0, 1])

def setup():
    datapath = "data1.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

setup()

def plotgraph():
    df = pd.read_csv("data1.csv")
    fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
    fig.show()

plotgraph()