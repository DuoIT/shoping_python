from django.conf.urls import url
from . import views
from .views import LoginClass

urlpatterns = [
    url(r'index/', views.index, name="index"),
    url(r'register/', views.register, name="register"),
    url(r'login/', LoginClass.as_view(), name="login"),
]
