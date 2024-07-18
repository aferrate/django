from django.shortcuts import render        
from django.http import HttpResponse
from datetime import datetime
from stocks.models import Call
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

    data = yf.download(name,date_start,date_end)['Adj Close']

    if len(data) == 0:
        return HttpResponse('error downloading data')

    df_list = []
    df_list.append(data)
    df = pd.concat(df_list)
    df.drop_duplicates()

    df.to_csv('list.csv', mode='a', header=False)

    call = Call(name_company=name)
    call.save()

    return HttpResponse('ok')

def index(request):
    return HttpResponse('<p><a href="/admin">admin</a></p><p><a href="/getstock/AAPL/2024-07-10/2024-07-11">stocks</a></p>')