from django.urls import path
from .views import user_admin_login, register, log_out, change_profile, user_list, active_deactive

urlpatterns = [
    path('user-admin-login', user_admin_login, name='user-admin-login'),
    path('register', register, name='register'),
    path('log_out', log_out, name='log_out'),
    path('change-profile', change_profile, name='change-profile'),
    path('user-list', user_list, name='user-list'),
    path('active-deactive', active_deactive, name='active-deactive'),
]
