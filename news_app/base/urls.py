from django.urls import path
# from .views import homepage
from . import views

app_name = "news_app"   

urlpatterns = [
    path('', views.login_request, name='news'),
    path("register", views.register_request, name="register"),
    path("homepage", views.homepage, name="homepage"),
    path("logout", views.logout_request, name= "logout"),
]

