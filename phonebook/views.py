import csv
import os
import datetime
import random

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .filters import DepartmentFilter
# Create your views here.
from phonebook.models import Customer, Subdepartment, Department
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def fetch_pdf_resources(uri, rel):
     if uri.find(settings.MEDIA_URL) != -1:
         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
     elif uri.find(settings.STATIC_URL) != -1:
         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
     else:
         path = None
     return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, encoding='utf-8', link_callback=fetch_pdf_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

data = {
     "departments": Department.objects.all(),
 }

class ViewPDF(View):
     def get(self, request, *args, **kwargs):
         pdf = render_to_pdf('pdf_first.html', data)
         return HttpResponse(pdf, content_type='application/pdf')


def centralOffice(request):
    departments = Department.objects.all()
    sub_departments = Subdepartment.objects.all()
    customers = Customer.objects.all()
    myFilter = DepartmentFilter(request.GET, queryset=departments)
    departments = myFilter.qs
    time = datetime.datetime.now()

    context = {"customers":customers, "departments":departments, 'sub_departments':sub_departments, 'myFilter':myFilter, 'time':time}
    return render(request, 'centralOffice.html', context)

def otherPage(request):
    return render(request, 'others.html')


def pdfTemplate(request):
    return render(request, 'pdf_first.html', {"departments": Department.objects.all()})


