from django.urls import path, include
from package.views import home
urlpatterns = [
    path('', home, name="home"),
]
