from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# class HomeView(View):
def index(request):
    return render(request, 'homepage/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register/index.html', {'form': form})


class LoginClass(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_customer = authenticate(username=user_name, password=pass_word)
        if my_customer is None:
            return HttpResponse("Username is not exits, login failed")
        login(request, my_customer)
        return render(request, 'homepage/index.html')

