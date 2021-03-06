from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                CreateView, UpdateView, DeleteView)
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION!'
    #     return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'index/school_list.html'
    #school list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'index/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    template_name = 'index/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    template_name = 'index/school_form.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
    template_name = 'index/school_confirm_delete.html'
