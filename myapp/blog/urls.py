from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("detail/<int:pk>", views.Detail.as_view(), name='detail'),
    path("write/", views.Write.as_view(), name='write'),
    path("",views.get, name='list')
]