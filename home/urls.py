from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('age-5-7/', views.age_5_7, name='age_5_7'),
    path('age-8-10/', views.age_8_10, name='age_8_10'),
    path('age-11-12/', views.age_11_12, name='age_11_12'),
    path('quiz/<int:pk>/', views.quiz_view, name='quiz'),   # 👈 add this
]
