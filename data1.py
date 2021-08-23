import pandas as pd
import plotly.express as px

df = pd.read_csv("data1.csv")
fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
fig.show()