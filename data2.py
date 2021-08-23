import plotly.express as px
import pandas as pd    
import numpy as np
import csv

def getDataSource(datapath):
    sizeOfTV = []
    time = []
    with open (datapath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            sizeOfTV.append(float(i["SizeofTV"]))
            time.append(float(i["WatchTime"]))

    return{"x": sizeOfTV, "y": time}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Temperature and Ice-cream Sales is: ", correlation[0, 1])

def setup():
    datapath = "data2.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)

setup()

def plotGraph():
    with open("data2.csv") as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "SizeofTV", y = "WatchTime")
        fig.show()

plotGraph()