from django.shortcuts import render, get_object_or_404
from .models import Template
import os

def homepage(request):
    print("6, Homepage view called")  # Debug statement
    footer_template = get_object_or_404(Template, title='Footer')
    print("8, Footer template retrieved:", footer_template.content)  # Debug statement
    return render(request, 'home/home_page.html', {'footer_template': footer_template})
