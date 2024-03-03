from django.shortcuts import render


def sda(request):
    return render(request, 'blog/sda.html')