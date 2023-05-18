from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
"""from django.views.generic import TemplateView
class CBV_html(TemplateView):
    template_name='CBV_html.html'"""


class cbv_context(TemplateView):
    template_name='cbv_context.html'
    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']='mohana'
        EDCO['age']='21'
        return EDCO


class cbv_forms(TemplateView):
    template_name='cbv_forms.html'
    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['TFO']=TopicForm()
        return  EDCO
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        return HttpResponse('data is inserted')