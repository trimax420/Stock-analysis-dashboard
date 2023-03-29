from django.shortcuts import render  
from django.http import HttpResponse 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import yfinance as yf
from yahoofinancials import YahooFinancials
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
from pandas_datareader.data import DataReader
from datetime import datetime
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
for stock in tech_list:   
    globals()[stock] = yf.download(stock,start,end,progress=False)
company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name
df = pd.concat(company_list, axis=0)
ma_day = [10, 20, 50]
for ma in ma_day:
    for company in company_list:
        column_name = f"MA for {ma} days"
        company[column_name] = company['Adj Close'].rolling(ma).mean()

import plotly.express as px
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
'''
figures = [
            px.line(df1),
            px.line(df2)
    ]

fig = make_subplots(rows=len(figures), cols=1) 

for i, figure in enumerate(figures):
    for trace in range(len(figure["data"])):
        fig.append_trace(figure["data"][trace], row=i+1, col=1)
        
plot(fig)
'''

def index(request):
    return render(request,"index.html")

def contents(request):
    return render(request,"contents.html")

def about(request):
    return render(request,"about.html")    

def apple(request):
    def apple_stock():
        df = AAPL[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        
        fig = px.line(df) 
        graphic = plot(fig, output_type='div')
        return graphic

    apple=apple_stock()

    return render(request,"apple.html",{'apple':apple})  

def amazon(request):
    def amazon_stock():
        df = AMZN[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        
        fig = px.line(df) 
        graphic = plot(fig, output_type='div')
        return graphic

    amazon=amazon_stock()

    return render(request,"amazon.html",{'amazon':amazon}) 


def microsoft(request):
    def microsoft_stock():
        df = MSFT[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        
        fig = px.line(df) 
        graphic = plot(fig, output_type='div')
        return graphic

    microsoft=microsoft_stock()

    return render(request,"microsoft.html",{'microsoft':microsoft})          




def google(request):
    
    def google_stock():
        df = GOOG[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        
        fig = px.line(df) 
        graphic = plot(fig, output_type='div')
        return graphic

    google=google_stock()
    
    return render(request,"google.html",{'google':google})

def sales(request):
    def sales_result():
        plt.figure(figsize=(15, 7))
        plt.subplots_adjust(top=1.25, bottom=1.2)
        for i, company in enumerate(company_list, 1):
            plt.subplot(2, 2, i)
            company['Volume'].plot()
            plt.ylabel('Volume')
            plt.xlabel(None)
            plt.title(f"Sales Volume for {tech_list[i - 1]}")
        plt.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')

        return graphic

    def stock():
        #fig, axes = plt.subplots(nrows=2, ncols=2)
        #fig.set_figheight(8)
        #fig.set_figwidth(15)
        df_1=AAPL[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        df_2=GOOG[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        df_3=MSFT[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]
        df_4=AMZN[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']]

        plt1 = px.line(df_1,title='APPLE')
        plt2 = px.line(df_2,title='GOOGLE')
        plt3 = px.line(df_3,title='MICROSOFT')
        plt4 = px.line(df_4,title='AMAZON')
        
        graphic1 = plot(plt1, output_type='div')
        graphic2 = plot(plt2, output_type='div')
        graphic3 = plot(plt3, output_type='div')
        graphic4 = plot(plt4, output_type='div')

        return graphic1 ,graphic2, graphic3 , graphic4

    sales =sales_result()
    stock1,stock2,stock3,stock4=stock()
    return render(request,"sales.html",{'sales':sales,'stock1':stock1,'stock2':stock2,'stock3':stock3,'stock4':stock4})
