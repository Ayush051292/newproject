from django.urls import path
# from django.conf.urls import urls
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login_page),
    path('logout/', views.logout_page),
    path('home/', views.index),
    path('user_index/', views.user_index),
    path('user_add/', views.user_add),
    path('user_testing/', views.user_testing),
    path('user_edit/<id>/', views.user_edit),
    path('user_show/<id>/', views.user_show),
    path('user_delete/<id>/', views.user_delete),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)