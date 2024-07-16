from django.shortcuts import render        
from django.http import HttpResponse
from datetime import datetime
import yfinance as yf
import pandas as pd
        
def get_stock(request, name, date_start, date_end):
    format = '%Y-%m-%d'

    try:
        datetime.strptime(date_start, format)
    except ValueError:
        return HttpResponse('date start bad format, format must be YYYY-MM-DD')

    try:
        datetime.strptime(date_end, format)
    except ValueError:
        return HttpResponse('date end bad format, format must be YYYY-MM-DD')

    data = yf.download(name,'2016-01-01','2016-08-01')['Adj Close']

    if len(data) == 0:
        return HttpResponse('error downloading data')

    df_list = []
    df_list.append(data)
    df = pd.concat(df_list)
    df.to_csv('list.csv')

    return HttpResponse('ok')

def index(request):
    return HttpResponse('<p><a href="/admin">admin</a></p><p><a href="/getstock/AAPL/2020-01-01/2020-02-01">stocks</a></p>')