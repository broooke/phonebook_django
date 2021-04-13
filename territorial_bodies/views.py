
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from django.contrib.auth import authenticate, login, logout
import os
from django.contrib.auth.decorators import login_required
from .forms import signinForm, addCustomerForm, addSubdepartmentForm
# Create your views here.
from territorial_bodies.filters import DepartmentFilter
from territorial_bodies.models import Department, Customer, Subdepartment
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.conf import settings
from django.views.generic import DetailView



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
    print(pdf)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

data = {
     "departments": Department.objects.all(),
 }

class ViewPDF(View):
     def get(self, request, *args, **kwargs):
         pdf = render_to_pdf('pdf_second.html', data)
         return HttpResponse(pdf, content_type='application/pdf')

class ViewDetailPDF(DetailView):
    model = Department
    slug_field = "id"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        pdf = render_to_pdf('pdf_detail_2.html', self.get_context_data())
        return HttpResponse(pdf, content_type='application/pdf')


def mainPage(request):
    departments = Department.objects.all()
    sub_departments = Subdepartment.objects.all()
    customers = Customer.objects.all()
    myFilter = DepartmentFilter(request.GET, queryset=departments)
    departments = myFilter.qs
    time = datetime.now()

    context = {"customers": customers, "departments": departments, 'sub_departments': sub_departments, 'myFilter': myFilter, 'time':time}
    return render(request, 'territorial_bodies.html', context)

def pdfTemplate2(request):
    return render(request, 'pdf_second.html', {'departments': Department.objects.all()})

def detailDepartment(request, pk):
    department = Department.objects.get(id=pk)
    time = datetime.now()

    context = {'department':department, 'time':time}
    return render(request, 'detailDepartmentInfo.html', context)


def signinUser(request):
    if request.method == 'POST':
        form = signinForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('central-office')
    else:
        form = signinForm()

    context = {'form': form}

    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('central-office')

@login_required(login_url='login')
def detailsDepartment(request):
    group = request.user.groups.all()[0].name
    department = Department.objects.get(name=group)

    context = {'department': department}

    return render(request, 'detailsDepartment.html', context)

@login_required(login_url='login')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('details')

@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = addCustomerForm(instance=customer)
    group = request.user.groups.all()[0].name
    department = Department.objects.get(name=group)
    form.fields['subdepartment'].queryset = department.sub_department.all()
    if request.method == 'POST':
        form = addCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('details')

    context = {'form':form, 'customer':customer}

    return render(request, 'updateCustomer.html', context)

@login_required(login_url='login')
def createCustomer(request):
    form = addCustomerForm()
    group = request.user.groups.all()[0].name
    department = Department.objects.get(name=group)
    form.fields['subdepartment'].queryset = department.sub_department.all()
    if request.method == 'POST':
        form = addCustomerForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.department = department
            form_save.save()
            return redirect('details')

    context = {'form': form}
    return render(request, 'createCustomer.html', context)

@login_required(login_url='login')
def deleteSubdepartment(request, pk):
    subdepartment = Subdepartment.objects.get(id=pk)
    department = Department.objects.get(name=request.user.groups.all()[0].name)
    subdepartment.department.remove(department)
    if len(subdepartment.department.all()) == 0:
        subdepartment.delete()

    return redirect('details')

@login_required(login_url='login')
def createSubdepartment(request):
    if request.method == 'POST':
        department = Department.objects.get(name=request.user.groups.all()[0].name)
        form = addSubdepartmentForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            form_save.department.add(department)
            return redirect('details')
    else:
        form = addSubdepartmentForm()

    context = {'form':form}
    return render(request, 'createSubdepartment.html', context)

@login_required(login_url='login')
def updateSubdepartment(request, pk):
    department = Subdepartment.objects.get(id=pk)
    if request.method == 'POST':
        form = addSubdepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form = addSubdepartmentForm(instance=department)

    context = {'form': form, 'sub_dep':department}
    return render(request, 'updateSubdepartment.html', context)
