from django.urls import path
from firebase import views

urlpatterns = [
    path('', views.snippet_list),
    path('load', views.table_loader),
    path('<str:model>', views.snippet_detail),
    path('query/<int:id>', views.query_loader),
]
