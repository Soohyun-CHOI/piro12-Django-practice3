from django.shortcuts import render, redirect
from diary.models import Article


def list(request):
    """
    import datetime

    start_date = datetime.datetime(2020, 1, 18, 7) # 오후 4시
    end_date = datetime.datetime(2020, 1, 18, 8) # 오후 5시
    # .filter(created_at__range=(start_date, end_date))  시작일에서 마지막일 사이에 작성된 글들만
    # .filter(created_at__lt=end_date)    less than
    # .filter(created_at__gt=start_date)  greater than

    # .filter(title__startswith="p")  제목이 p로 시작하는 글들만
    # .filter(content__contains="1")  내용에 1이 들어가는 글들만
    # .filter(content__icontains="abc")  정확하게 포함하지 않아도 됨
    """

    queryset = Article.objects.all().order_by("-id")  # 내림차순 정렬

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


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        article = Article.objects.create(title=title, content=content)
        return redirect("articles-read", article.id)

    return render(request, "diary/create.html")  # request.method == GET


def update(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "GET":
        ctx = {
            "article": article
        }
        return render(request, "diary/update.html", ctx)

    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        article.title = title
        article.content = content
        article.save()

        return redirect("articles-read", article.id)


def delete(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "GET":
        return redirect("articles-read", article.id)

    elif request.method == "POST":
        article.delete()
        return redirect("articles-list")