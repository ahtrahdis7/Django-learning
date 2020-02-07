from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,
                                    DeleteView)  
# Create your views here.
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School



class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    template_name = 'basic_app/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    template_name = 'school_conf_delete.html'
    success_url = reverse_lazy('basic_app:list')
