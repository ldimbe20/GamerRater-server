from django.urls import path
from .views import GamePerCategory

urlpatterns = [
    path('reports/rating', GamePerCategory.as_view()),
]

