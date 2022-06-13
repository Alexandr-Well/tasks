from django.urls import path

from .views import ColorView, QuadraticEq

urlpatterns = [
    path('colors/', ColorView.as_view(), name='color'),
    path('quadratic_eq/', QuadraticEq.as_view(), name='quadratic_eq'),
]
