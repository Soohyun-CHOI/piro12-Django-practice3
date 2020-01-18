from django.shortcuts import render
from diary.models import Article


def list(request):
    queryset = Article.objects.all()
    ctx = {
        "articles": queryset
    }
    return render(request, "diary/list.html", ctx)


def read(request, pk):
    article = Article.objects.get(id=pk)
    ctx = {
        "article": article
    }
    return render(request, "diary/read.html", ctx)