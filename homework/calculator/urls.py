from django.urls import path
from . import views

urlpatterns = [
    path('factorial/<int:n>/', views.factorial, name='factorial'),
]
