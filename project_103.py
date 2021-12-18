import pandas as pd
import plotly.express as px

df = pd.read_csv("project_103.csv")

fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "Covid cases around the world!")

# fig = px.bar(df, x = "cases", y = "date", color = "country", title = "Covid cases around the world!")

# fig = px.line(df, x = "date", y = "cases", color = "country", title = "Covid cases around the world!")

fig.show()