from django.db import models


class Book(models.Model):
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name
# Create your models here.
class Impression(models.Model):
    """感想"""

    """
    Bookモデルを参照するために明示的に指定
    on_delete=models.CASCADEを指定することでBookモデルの該当行が削除されると、
    削除した行がが参照しているImpressionモデルの行を自動的に削除できる。
    """
    book = models.ForeignKey(Book, verbose_name='書籍名', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment