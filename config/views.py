from pprint import pp

from django.shortcuts import redirect, render


def homeView(request):
    if request.user.is_authenticated:
        return redirect('users:detail', request.user.username)
    return render(request, 'pages/home.html')
