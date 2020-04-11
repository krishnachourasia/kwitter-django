from .views import (home,
                    about)
from django.urls import path


urlpatterns = [
    path('', home, name='blog-home'),
    path("about/", about, name='blog-about')
]
