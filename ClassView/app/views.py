from django.shortcuts import render
from django.http import HttpResponse
from app.forms import*
from django.views.generic import TemplateView,View


# Create your views here.
# class Insert_School_bycbv(View):
#     def get(self, request):
#         ESFO = SchoolForm()
#         d = {'ESFO':ESFO}
#         return render(request, 'Insert_School_bycbv.html', d)
    
#     def post(self, request):
#         SFDO = SchoolForm(request.POST)
#         SFDO.save()
#         return HttpResponse('School Created Successfully')
    

    
# from django.db import IntegrityError
from django.http import HttpResponseServerError

class Insert_School_bycbv(View):
    def get(self, request):
        ESFO = SchoolForm()
        d = {'ESFO': ESFO}
        return render(request, 'Insert_School_bycbv.html', d)
    
    def post(self, request):
        SFDO = SchoolForm(request.POST)
        try:
            SFDO.save()
            return HttpResponse('School Created Successfully')
        except :
            return HttpResponseServerError('Primary key or sname already exists. School creation failed.')



class Template(TemplateView):
    template_name='template.html'
