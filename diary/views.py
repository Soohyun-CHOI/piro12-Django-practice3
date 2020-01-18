from django.shortcuts import render


def list(request):
    render(request, "diary/list.html")