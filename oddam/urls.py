from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),



]
