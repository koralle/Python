from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 一覧表示
def index(request):
    return HttpResponse("一覧")

# 新規追加、編集
def edit(request, id=None):
    return HttpResponse("編集")

# 削除
def delete(request, id=None):
    return HttpResponse("削除")

# 詳細
def detail(request, id=None):
    return HttpResponse("詳細")