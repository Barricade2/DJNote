from django.shortcuts import render, get_object_or_404, redirect
from apps.index.forms import UserLoginForm
from django.contrib.auth import login, logout


def index(request):
	return render(request, 'index/index.html')

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('note:note')
	else:
		form = UserLoginForm()
	return render(request, 'index/login.html', {"form": form})