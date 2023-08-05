from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index),
    path('add/', views.add),
    path('edit/<id>/', views.edit),
    path('show/<id>/', views.show),
    path('delete/<id>/', views.delete),
    path('autosave/',views.autosave, name="autosave")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)