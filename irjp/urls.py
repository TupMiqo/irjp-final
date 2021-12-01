from django.urls import path

from . import views

urlpatterns = [
    # read views.py and execute index function
    # read views.py and execute menu function
    path('', views.home, name='Home'),
    path('Home', views.home, name='Home'),
    path('register', views.Register, name='Register'),
    path('login2', views.login2, name='login2'),
    path('table', views.table, name='table'),
    path('edit/<data_id>/', views.edittable, name='edit'),
    path('delete/<data_id>/', views.delete_data, name='delete')
    

]   
