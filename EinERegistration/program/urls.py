from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:program_title>/', views.levels, name='levels'),
    path('<str:program_title>/level_<str:program_level>/upcoming_sessions',
         views.iterations, name='iterations')
]

# I am unsure what these three parameters do ^

