# Task 3
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

# Print the first and last 10 lines of the DataFrame
print(df.head(10))
print(df.tail(10))

df["strength"] = df["strength"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
print(df["strength"].dtype)

fig = px.scatter(df, x="strength", y="frequency", color="direction", title="Wind Strength vs Frequency")
fig.write_html("wind.html", auto_open=True)
