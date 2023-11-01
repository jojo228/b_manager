from django.http import HttpResponse
from django.shortcuts import redirect


def auth_users(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.staff_type == "ENT":
                return redirect("profil")
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Vous n'êtes pas authorisé à visiter cette page")

        return wrapper

    return decorators
