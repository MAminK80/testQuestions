from django.urls import path
from . import views

app_name = 'question'
urlpatterns = [
    path('all_questionnaires/', views.QuestionnaireListView.as_view(), name='all_questionnaires'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
]
