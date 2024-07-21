from django.shortcuts import render        
from django.http import HttpResponse
from datetime import datetime
from stocks.models import Call
import yfinance as yf
import pandas as pd
        
def get_stock(request, name, date_start_str, date_end_str):
    format = '%Y-%m-%d'

    try:
        date_start = datetime.strptime(date_start_str, format)
    except ValueError:
        return HttpResponse('date start bad format, format must be YYYY-MM-DD')

    try:
        date_end = datetime.strptime(date_end_str, format)
    except ValueError:
        return HttpResponse('date end bad format, format must be YYYY-MM-DD')

    if date_start > date_end:
        return HttpResponse('start date cannot be greater than end date')

    today = datetime.today().date()

    if date_start.date() > today or date_end.date() > today:
        return HttpResponse('dates cannot be greater than today')

    data = yf.download(name, date_start_str, date_end_str)

    if len(data) == 0:
        return HttpResponse('error downloading data')

    df_list = []
    data['Name'] = name

    df_list.append(data)

    df_csv = pd.read_csv('list.csv')

    df_csv = pd.concat(df_list)

    df_csv.to_csv('list.csv', mode = 'a', header = False)

    call = Call(name_company=name)
    call.save()

    return HttpResponse('ok')

def index(request):
    return HttpResponse('<p><a href="/admin">admin</a></p><p><a href="/getstock/AAPL/2024-07-10/2024-07-11">stocks</a></p>')