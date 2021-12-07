import plotly.express as px 
import csv
import numpy as np 

with open ("./Data/CoffeVsSleep.csv") as csv_file :
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffee in ml",y="sleep in hours") 
    fig.show()

def getDataSource (data_path) :
    coffee_increase = []
    sleep_hours = []
    with open(data_path)as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            coffee_increase.append (float(row["Coffee in ml"]))
            sleep_hours.append (float(row["sleep in hours"])) 
    return{"x":coffee_increase,"y":sleep_hours}   

def findCorrelation (dataSource) : 
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between coffe Vs Sleep : /n",correlation[0,1])

def setup ():
    data_path = "./Data/CoffeVsSleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource) 

setup()    