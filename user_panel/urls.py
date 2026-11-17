from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserView.as_view(),name ='user_panel'),
    path('user/edit-profile', views.EditProfileView.as_view(),name ='user-edit-profile'),
    path('user/change-password', views.ChangePasswordView.as_view(),name ='user_change_password'),
]
