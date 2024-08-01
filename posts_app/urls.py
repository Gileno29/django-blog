from django.urls import path
from . import views

urlpatterns =[
    path('', views.post_list, name='post-list'),
    path('post-create', views.post_create, name='post-create'),
     path('post-datail', views.post_create, name='post-detail'),

]
