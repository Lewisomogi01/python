from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('books/', include('book_api.urls'))
]
