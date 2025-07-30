from django.shortcuts import render
from .models import Users
from .forms import SearchForm
from django.template.context_processors import request
from django.template.defaulttags import comment
from django.core.paginator import Paginator


# def index(request, department=None):
#
#     query = None
#     result = []
#     print(request.GET)
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             result = Users.objects.filter(name__icontains=query)
#
#     if department:
#         posts = Users.objects.filter(department=department)
#     elif result:
#         posts = Users.objects.filter(result=result)
#     else:
#         posts = Users.objects.all()
#     # paginator = Paginator(posts, 2)
#     # page = request.GET.get('page')
#     # user_info = paginator.get_page(page)
#     return render(request, "phone/info.html", {'user_info': posts})





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








# def user_search(request):
#     query = None
#     result = []
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             result = Users.objects.filter(name__icontains=query)
#     context = {
#         'query': query,
#         'result': result,
#     }
#     return render(request, 'phone/info.html', context)

