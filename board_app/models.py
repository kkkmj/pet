from django.db import models

# Create your models here.
class Board(models.Model):
    author = models.CharField(max_length=10, null=False) # 작성자
    title = models.CharField(max_length=100, null=False) # 제목
    content = models.TextField(null=False) # 본문
    created_date = models.DateTimeField(auto_now_add=True) # 글 작성 시간
    modified_date = models.DateTimeField(auto_now=True) # 글 수정 시간

class sub_Board(models.Model):
    board = models.ForeignKey(Board, on_delete = models.CASCADE, null=True)
    content = models.TextField(null=False) # 본문
    created_date = models.DateTimeField(auto_now_add=True) # 글 작성 시간