from django.forms import ModelForm
from todo.models import ToDo

class ToDoForm(ModelForm):

    class Meta:
        # データを登録したいモデルを指定する。
        model = ToDo

        # フォームで入力したいデータを指定する。
        fields = ('deadline', 'title', 'content')