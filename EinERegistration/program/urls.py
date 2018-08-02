from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:program_title>/', views.details, name='details'),
    path('<str:program_title>/level_<str:level_id>/upcoming_sessions',
         views.iterations, name='iterations')
]

# I am unsure what these three parameters do ^

