from django.shortcuts import render
from .models import Users
from .forms import SearchForm
from django.template.context_processors import request
from django.template.defaulttags import comment
from django.core.paginator import Paginator



def index(request, department=None):
    query = request.GET.get('query')
    print(query)
    if department:
        users = Users.objects.filter(department=department)
        if query:
            users = Users.objects.filter(name__icontains=query)

    elif query:
        users = Users.objects.filter(name__icontains=query)
    else:
        users = Users.objects.all()

    return render(request, "phone/info.html", {'user_info': users})

