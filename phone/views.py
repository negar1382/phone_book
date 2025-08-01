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
        users = Users.objects.filter(department=department).order_by('name')
        if query:
            users = Users.objects.filter(name__icontains=query).order_by('name')

    elif query:
        users = Users.objects.filter(name__icontains=query).order_by('name')
    else:
        users = Users.objects.all().order_by('name')

    return render(request, "phone/info.html", {'user_info': users})

