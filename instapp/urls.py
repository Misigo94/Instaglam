from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
   path('', views.home, name="home"),
   path('login/', views.login_user, name="login"),
   path('logout/', views.logout_user, name="logout"),
   path('register/', views.register_user, name="register"),
   path('profile/', views.upload_profile, name="profile"),
]