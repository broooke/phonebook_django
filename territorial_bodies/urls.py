
from django.urls import path

from territorial_bodies import views

urlpatterns = [
    path('', views.mainPage, name='second-page'),
    path('pdf_download/', views.ViewPDF.as_view(), name="pdf_download_2"),
    path('pdf/template/', views.pdfTemplate2, name='pdf-template-2'),
    path('login/', views.signinUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('details/', views.detailsDepartment, name='details'),
    path('delete/<str:pk>/', views.deleteCustomer, name='delete-customer'),
    path('update/<str:pk>/', views.updateCustomer, name='update-customer'),
    path('create/', views.createCustomer, name='create-customer'),
    path('delete/sub-department/<str:pk>/', views.deleteSubdepartment, name='delete-subdepartment'),
    path('create/subdepartment/', views.createSubdepartment, name='create-subdepartment'),
    path('update/subdepartment/<str:pk>/', views.updateSubdepartment, name='update-subdepartment'),
    path('detail/<str:pk>/', views.detailDepartment, name='details-dep'),
    path('pdf_download/<slug:slug>/', views.ViewDetailPDF.as_view(), name="pdf_download_detail_2"),
]
