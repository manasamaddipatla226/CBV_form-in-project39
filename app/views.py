from django.shortcuts import render
from app.forms import *
from django.views.generic import FormView
from django.http import HttpResponse
from app.models import *

# Create your views here.

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=SchoolForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('data is submitted successfully')


