from django.conf.urls import url
from .views import welcome

urlpatterns = [
    url(r'welcome$',welcome, name="welcome"),
    
]