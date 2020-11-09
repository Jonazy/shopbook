from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.home, name='index'),
    path('category/<slug:category_slug>/', views.home, name='book_by_category'),
    path('<slug:slug>/', views.detail, name='book_detail'),

]