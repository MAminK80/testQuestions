from django.urls import path
from .views import StudentView, ShowScoreView, CategoryView

urlpatterns = [
    path('', StudentView.as_view(), name='student_view'),
    path('score/', ShowScoreView.as_view(), name='score'),
    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
]
