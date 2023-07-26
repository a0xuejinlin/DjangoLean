import json
import sqlite3
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import baostock as bs
import pandas as pd

# Create your views here.

def index(request):
    return HttpResponse("Hello,world.you're at the polls index.")

# stockserver/views.py
def spec(request):
    specname = request.GET.get('specname', 'amplitude_10')
    order = request.GET.get('order', 'desc')
    isAbs = request.GET.get('abs', 'false')
    orderbyvalue = specname
    if isAbs == 'true':
        orderbyvalue = "abs(" + specname + ")"
    print(specname, order, isAbs, orderbyvalue)
    cx = sqlite3.connect(r'D:\gtst\datasx3\mystock.db')
    sql_cmd = "SELECT * FROM stock_spec where date=(select max(date) from stock_spec) and " + specname + " != 'NaN' order by " + orderbyvalue + " " + order + " limit 0,50"
    
    result = pd.read_sql(sql=sql_cmd, con=cx)
    df_json = result.to_json(orient = 'table', force_ascii = False)
    data = json.loads(df_json)

    return JsonResponse(data, safe=False)

# stockserver/views.py
def dayk(request):
    codename = request.GET.get('code', 'sh.000001')
    order = 'desc'
    print(codename, order)
    cx = sqlite3.connect(r'D:\gtst\datasx3\mystock.db')
    sql_cmd = "SELECT * FROM stock_day_k where code='" + codename +"' order by date desc limit 0,365"
    
    result = pd.read_sql(sql=sql_cmd, con=cx)
    df_json = result.to_json(orient = 'table', force_ascii = False)
    data = json.loads(df_json)

    return JsonResponse(data, safe=False)