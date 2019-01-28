from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import json

a = "94.10.26.6"

def home(request):
    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("SELECT * FROM locationindex")

    data = (dict(location = row[0], x = row[1], y = row[2], value1 = row[3], value2 = row[4], color1 = row[5], color2 = row[6], pick1 = row[7], pick2 = row[8]) for row in cur)
    
    data = []
    for i in cur:
        values = {
            "loc": i[0],
            "xpos": i[1],
            "ypos": i[2],
            "value1": i[3],
            "color1": i[5],
            "pick1": i[7],
            "value2": i[4],
            "color2": i[6],
            "pick2": i[8]


            }
        data.append(values)
    

    return render(request, 'home/home.html', {"data":data})

def about(request):
    picloc = request.POST.get("data1")
    product = request.POST.get("data2")

    

    xp = request.POST.get("data3")
    yp = request.POST.get("data4")

    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("UPDATE locationindex SET value1 = %s, pick = %s WHERE x = %s AND y = %s",(product, picloc, xp, yp))
    conn.commit()

    

    
    return HttpResponse("nothing")
# Create your views here.
