from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.list import ListView

from todo.models import ToDo
from todo.forms import ToDoForm

# Create your views here.

def todo_list_view(request):
    # 期限の近い順に並べる
    todo = ToDo.objects.all().order_by('deadline')
    return render(request,
        'todo/todo_list_view.html',
        {'todo':todo}
    )


def todo_list_add(request):
    return HttpResponse("タスク追加")

def todo_list_edit(request, todo_id=None):
    # todo_idが指定されている場合⇒todo項目の修正
    if todo_id:
        todo = get_object_or_404(klass=ToDo, pk=todo_id)

    # todo_idが指定されていない⇒todo項目の追加
    else:
        todo = ToDo()

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)

        # フォームのバリデーションの実行
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list_view')
    else:
        form = ToDoForm(instance = todo)

    return render(request, 'todo/todo_edit.html', dict(form=form, todo_id=todo_id))

def todo_list_delete(request, todo_id=None):
    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()
    return redirect('todo:todo_list_view')

