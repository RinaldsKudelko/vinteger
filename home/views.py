from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from django.http import JsonResponse

a = "94.10.26.6"

def home(request):
    conn = pymysql.connect(host = a, user = "root", password = "51379028", db = "database")
    cur = conn.cursor()
    cur.execute("SELECT * FROM rack")

    data = (dict(product = row[0], loc = row[1], pickloc = row[2], xpos = row[3], ypos = row[4]) for row in cur)
    
    data = []
    for i in cur:
        values = {
            "product": i[0],
            "loc": i[1],
            "pickloc": i[2],
            "xpos": i[3],
            "ypos": i[4]
            }
        data.append(values)
    

    return render(request, 'home/home.html', {"data":data})

def about(request):
    
    return HttpResponse('home/about.html')
# Create your views here.
