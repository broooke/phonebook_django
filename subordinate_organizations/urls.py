from django.urls import path

from subordinate_organizations import views

urlpatterns = [
    path('', views.mainPage, name='third'),
    path('pdf_download/', views.ViewPDF.as_view(), name="pdf_download_3"),
    path('pdf/template/', views.pdf_template, name='pdf-template-3'),
    path('details/', views.detailsDepartment, name='details-1'),
    path('delete/<str:pk>/', views.deleteCustomer, name='delete-customer-1'),
    path('update/<str:pk>/', views.updateCustomer, name='update-customer-1'),
    path('create/', views.createCustomer, name='create-customer-1'),
    path('delete/sub-department/<str:pk>/', views.deleteSubdepartment, name='delete-subdepartment-1'),
    path('create/subdepartment/', views.createSubdepartment, name='create-subdepartment-1'),
    path('update/subdepartment/<str:pk>/', views.updateSubdepartment, name='update-subdepartment-1'),
    path('details/<str:pk>/', views.detailDepartment, name='detail-dep-2'),
    path('pdf_download/<slug:slug>/', views.ViewDetailPDF.as_view(), name="pdf_download_detail_3"),
]
