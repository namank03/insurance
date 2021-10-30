from django.shortcuts import redirect, render


def homeView(request):
    print('inside home view')
    if request.user.is_authenticated:
        print('inside authenticated')
        return redirect("users:detail", request.user.username)
    return render(request, "pages/home.html")
