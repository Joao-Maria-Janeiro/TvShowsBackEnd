from django.urls import path, include
from . import views
from rest_framework.authtoken import views as at_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('get-token', at_views.obtain_auth_token, name="get-token"),
    path('add', csrf_exempt(views.add_show), name="add"),
    path('list', views.get_user_list, name="list"),
    path('list/<str:username>', views.get_user_list_name, name="list_name"),
    path('suggest', csrf_exempt(views.make_suggestion), name="suggest"),
    path('suggestions', views.get_suggestions, name="suggestions"), 
    path('integrate-suggestion', csrf_exempt(views.integrate_suggestion), name="integrate-suggestion"),       
]
