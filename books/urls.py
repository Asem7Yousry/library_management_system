from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('books/', show_books , name="all_books"),
    path('home/', show_home , name="show_home"),
    path('books/add_book/', add_new_book , name="add_new_book"),
    path('books/edit/<int:id>', edit_book , name="edit_book"),
    path('books/delete/<int:id>', delete_book , name="delete_book"),
]