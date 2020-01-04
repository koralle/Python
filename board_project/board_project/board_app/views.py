from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
  if request.method == 'POST':
    username2 = request.POST['username']
    password2 = request.POST['password']
    try:
      User.objects.get(username=username2)
      return render(request, 'signup.html', {'error': 'このユーザは登録されています。'})
    except:
      user = User.objects.create_user(username2, password2)
      return render(request, 'signup.html', {"some": 200})
    
  else:
    print("this is not post method")
  return render(request, 'signup.html', {"some": 100})

def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect("board_app:login")
    else:
        # Return an 'invalid login' error message.
        return redirect("board_app:list")
  return render(request, 'login.html', )

@login_required()
def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list': object_list})

def logoutfunc(request):
    logout(request)
    return redirect('board_app:login')
    # Redirect to a success page.

def detailfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  return render(request, 'detail.html', {'object': object })

def goodfunc(request, pk):
  post = BoardModel.objects.get(pk=pk)
  post.good += 1
  post.save()
  return redirect('board_app:list')

def readfunc(request, pk):
  post = BoardModel.objects.get(pk=pk)
  post2 = request.user.get_username()
  if post2 in post.readtext:
    return redirect('board_app:list')
  else:
    post.read += 1
    post.readtext = post.readtext + ' ' + post2
    return redirect(('board_app:list'))


class BoardCreate(CreateView):
  template_name = 'create.html'
  model = BoardModel
  fields = ('title', 'content', 'image', 'author')
  success_url = reverse_lazy('board_app:list')