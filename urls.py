from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrangChu, name="TrangChu"), 
    path("generate/", views.generate_exam, name="generate_exam"),
    path('huongdan/', views.huongdan, name='huongdan'),
    path('lichsu/', views.lichsu, name='lichsu'),
]
