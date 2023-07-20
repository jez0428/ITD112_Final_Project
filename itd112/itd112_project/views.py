from django.shortcuts import render
from collections import Counter
import pandas as pd
import plotly.graph_objects as go



# Create your views here.
def readfile(): #function to read the csv file

    global rows,columns,data,my_file,missing_values, attribute
    missingvalue = ['?', '0', '--']

    my_file = pd.read_csv('C:\\Users\\chris\\PycharmProjects\\ITD112_Final_Project\\itd112\\itd112_project\\media\\doh-epi-dengue-data-2016-2021.csv',
                                        sep='[:;,|_]',na_values=missingvalue, engine='python')


    attribute = 'Region' #attribute to display in the chart

    data = pd.DataFrame(data=my_file, index=None)

    rows = len(data.axes[0])
    columns = len(data.axes[1])

def index(request):
    readfile()

    dashboard = []
    for x in data[attribute]:
        dashboard.append(x)

    my_dashboard = dict(Counter(dashboard))

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for x in keys:
        listkeys.append(x)

    for y in values:
        listvalues.append(y)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, "itd112_project/index.html", context)

def project2(request):

    df = pd.read_csv('C:\\Users\\chris\\PycharmProjects\\ITD112_Final_Project\\itd112\\itd112_project\\media\\worldcities.csv')
    df['name'] = df['city']

    fig = go.Figure(data=go.Scattergeo(
        lon=df['lng'],
        lat=df['lat'],
        text=df['name'],
        mode='markers',
        marker=dict(
            color='#B76DF5',
            size=4,
            line=dict(
                color='#4C286A',
                width=1
            )
        )
    ))

    fig.update_geos(
        coastlinecolor="RebeccaPurple",
        coastlinewidth=1.5,
        landcolor="LightGreen",
        showocean=True, oceancolor="LightBlue",
    )


    fig.update_layout(paper_bgcolor="#F1F1F1")

    # Generate the SVG plot as an HTML div element
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'figure': plot_div,
    }
    return render(request, 'itd112_project/project2.html', context)


def project3(request):
    filename = 'C:\\Users\\chris\\PycharmProjects\\ITD112_Final_Project\\itd112\\itd112_project\\media\\Covid.csv'
    dataset = pd.read_csv(filename)
    # print(data.head())

    fig = go.Figure(data=[
        go.Bar(name='Confirmed', x=dataset['Country'], y=dataset['Confirmed']),
        go.Bar(name='Deaths', x=dataset['Country'], y=dataset['Deaths']),
        go.Bar(name='Recovered', x=dataset['Country'], y=dataset['Recovered']),
    ])

    # Change the bar mode
    fig.update_layout(
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor="#F1F1F1",
    )

    # Generate the SVG plot as an HTML div element
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'figure': plot_div,
    }
    return render(request, 'itd112_project/project3.html', context)
