from django.shortcuts import redirect, render


def home_view(request):
    if request.user.is_authenticated:
        return redirect("users:detail", request.user.username)
    return render(request, "pages/home.html")
