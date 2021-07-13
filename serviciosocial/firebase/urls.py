from django.urls import path
from firebase import views

urlpatterns = [
    path('', views.snippet_list),
    path('<str:model>', views.snippet_detail),
]
