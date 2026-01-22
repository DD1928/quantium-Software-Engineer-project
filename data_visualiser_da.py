import dash
import pandas as pd
import plotly.express as px

#open the xlsx file

df=pd.read_csv("pink_morsel_sales.csv")

#make sure the date col values are in datetime format
df["Date"]=pd.to_datetime(df["Date"])

#sort the df by date
df_sorted=df.sort_values("Date")


#intialise dash app
app=dash.Dash(__name__)

#plot using px line graph - confirm hover ?
fig=px.line(df_sorted,x="Date",y="Sales",title="Pink Morsel Sales by date")

app.layout = dash.html.Div(children=[
    # html.H1(children='Hello Dash'),
    #
    # html.Div(children='''
    #     Dash: A web application framework for your data.
    # '''),

    dash.dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)


#basic dash app completed
#add callbacks to make it better - try group by month and year