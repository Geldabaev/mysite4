from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

def index(request):
    return render(request, "blog/index.html")


def test(request):
    return render(request, "blog/test.html")


def categ(request, catid):
    return HttpResponse(f"<h1>Page {catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Аг1о кара ца йо</h1>")