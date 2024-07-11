from django.shortcuts import render, get_object_or_404
from .models import Template
import os

def homepage(request):
    footer_template = get_object_or_404(Template, title='Footer')
    return render(request, 'home/home_page.html', {'footer_template': footer_template})

def about(request):
    footer_template = get_object_or_404(Template, title='Footer')
    return render(request, 'home/about_page.html', {'footer_template': footer_template})
