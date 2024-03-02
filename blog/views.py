from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def test_fun(request):
    return render(request, "blog/test.html")


def categ(request):
    return render(request, "blog/categ.html")
