from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getData),
    path('add/', views.addItem),
    path('edit/<int:item_id>', views.editItem),
    path('delete/<int:item_id>', views.deleteItem),
]