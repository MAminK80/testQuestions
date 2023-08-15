from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('logout/', views.LogoutUser.as_view(), name='logout_user')
]
