from django.urls import path
from .views import FileView
urlpatterns = [
    path(r'^upload/$', FileView.as_view(), name='file-upload'),
]