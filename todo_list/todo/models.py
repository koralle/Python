from django.db import models

# Create your models here.
class ToDo(models.Model):
    # タスクID
    id = models.IntegerField(verbose_name='タスクID', primary_key=True)

    # 期限
    deadline = models.DateTimeField(verbose_name='期限')

    # タスク名
    title = models.TextField(verbose_name='タスク名', max_length=255)

    # タスク詳細
    content = models.TextField(verbose_name='タスク詳細', max_length=255, blank=True)

    def __str__(self):
        return self.title

