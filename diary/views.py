from django.shortcuts import render
from diary.models import Article


def list(request):
    queryset = Article.objects.all()
    ctx = {
        "articles": queryset
    }
    return render(request, "diary/list.html", ctx)