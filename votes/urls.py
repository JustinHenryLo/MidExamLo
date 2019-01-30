from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'votes'


urlpatterns = [
    path('',views.index,name ="index"),
    path('register',views.create,name ="create"),
    path('positions',views.create_position,name ="create_position"),
    path('<int:c_id>',views.detail,name ="detail"),
    #path('<int:post>',views.detail,name ="detail"),
    path('<int:c_id>/update',views.update,name ="update"),
    path('<int:c_id>/vote',views.vote,name ="vote"),
]

