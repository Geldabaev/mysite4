from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse, Http404


def index(request):
    return render(request, "blog/index.html")


def test(request):
    return render(request, "blog/test.html")

"http://127.0.0.1:8000/categ/1/?name=Yunus&age=27"
def categ(request, catid):
    if request.GET:
        print("Имя:", request.GET['name'])
        print("Возраст:", request.GET['age'])
    else:
        print("Нет данных")
    if int(catid) == 50:  # ручная генерация ошибки
        raise Http404
    if int(catid) == 1000:
        return redirect("home") # перенаправление
    if int(catid) == 500:
        return redirect("test", permanent=True)

    return HttpResponse(f"<h1>Page {catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Аг1о кара ца йо</h1>")