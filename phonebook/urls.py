from django.contrib import admin
from django.urls import path, include

from phonebook import views

urlpatterns = [
    path('', views.centralOffice, name='central-office'),
    path('other/', views.otherPage, name='other'),
    path('pdf_download/', views.ViewPDF.as_view(), name="pdf_download_1"),
    path('pdf-template/', views.pdfTemplate, name='pdf-template-1'),
]
