from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from django.http import JsonResponse
import json

a = "94.10.26.6"

def home(request):
    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("SELECT * FROM locationindex ORDER BY pick1, pick2 ASC")

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
    picloc1 = request.POST.get("data1")
    product1 = request.POST.get("data2")
    picloc2 = request.POST.get("data3")
    product2 = request.POST.get("data4")

    

    xp = request.POST.get("data5")
    yp = request.POST.get("data6")
    x = int(xp.replace("'", ""))
    y=int(yp.replace("'", ""))
    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("UPDATE locationindex SET value1 = %s, value2 = %s, pick1 = %s, pick2 = %s  WHERE x = %s AND y = %s",(product1, product2, picloc1, picloc2, x, y))
    conn.commit()

    

    
    return HttpResponse("nothing")


def celldata(request):
    row = request.POST.get("data1")
    cell = request.POST.get("data2")
    print(row, cell)
    x = int(row.replace("'", ""))
    y=int(cell.replace("'", ""))
    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("SELECT * FROM locationindex WHERE x = %s AND y = %s ORDER BY pick1, pick2 ASC",(x, y))
    
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
    

    
    
    return JsonResponse({"data":data})
# Create your views here.
