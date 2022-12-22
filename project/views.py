from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def registration(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        try:
            if User.objects.get(username=login):
                return render(request, 'registration/registration_form.html',
                      {'error_message': 'Пользователь уже зарегистрирован'})
        except:
            user = User.objects.create_user(login, login + '@mail.com', password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'registration/registration_form.html')