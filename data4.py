import pandas as pd
import plotly.express as px

df = pd.read_csv("data4.csv")
fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
fig.show()