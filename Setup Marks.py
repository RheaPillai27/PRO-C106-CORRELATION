import plotly.express as px 
import csv
import numpy as np 

with open ("./Data/StudentVsMarks.csv") as csv_file :
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Marks",y="Days") 
    fig.show()

def getDataSource (data_path) :
    Marks_got = []
    Days_present = []
    with open(data_path)as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
             Marks_got.append (float(row["Marks"]))
             Days_present.append (float(row["Days"])) 
    return{"x":Marks_got,"y": Days_present}   

def findCorrelation (dataSource) : 
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Marks Vs DaysPresent : /n",correlation[0,1])

def setup ():
    data_path = "./Data/StudentVsMarks.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource) 

setup()    