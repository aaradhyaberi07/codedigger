from django.urls import path
from .views import RegisterView,VerifyEmail,LoginApiView,ProfileGetView,ProfileUpdateView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/',RegisterView.as_view(),name = "register"),
    path('email-verify/',VerifyEmail.as_view(),name = "email-verify"),
    path('profile/',ProfileGetView.as_view(),name = "profile"),
    path('profile/<int:id>',ProfileUpdateView.as_view(),name = "profile"),
    path('login/',LoginApiView.as_view(),name = "login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
