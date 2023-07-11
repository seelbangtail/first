from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Hello")
И в файле urls.py эта функция соотносится с некоторым маршрутом:
'''
1
2
3
4
5
6
'''
from django.urls import path
from hello import views
 
urlpatterns = [
    path("", views.index),
]
