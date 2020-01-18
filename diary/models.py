from django.db import models


# 일기
# - 제목
# - 내용
# - 작성한 날짜
# - 이미지


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="일기 제목", help_text="일기 제목")
    content = models.TextField(verbose_name="일기 내용", help_text="일기 내용")

    created_at = models.DateTimeField()
    # DateField: 날짜만
    # DateTimeField: 날짜 + 시간