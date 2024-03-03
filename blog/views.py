from django.shortcuts import render

def index(request):
    return render(request, "blog/robot.html")

def test(request):
    return render(request, "blog/test.html")