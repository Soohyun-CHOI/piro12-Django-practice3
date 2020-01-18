from django.db import models


# 일기
# - 제목
# - 내용
# - 작성한 날짜
# - 이미지


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="일기 제목", help_text="일기 제목")
    content = models.TextField(null=True, blank=True, verbose_name="일기 내용", help_text="일기 내용")
    image = models.ImageField(null=True, blank=True, upload_to="images", verbose_name="일기 이미지", help_text="일기 이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일", help_text="작성일")
    # DateField: 날짜만
    # DateTimeField: 날짜 + 시간
