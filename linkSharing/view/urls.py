from django.urls import path

from . import views


app_name='view'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', LinkList.as_view()),
]
