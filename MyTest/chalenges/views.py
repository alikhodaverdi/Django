from ast import arg
from django.shortcuts import redirect, render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse ## bar assas adresi ke barash dar nazar gerfrim adres ro bar migradone
# Create your views here.

days = {
    'saturday' : 'this is saturedday',
    'sunday' : 'this is saturedday',
    'monday' : 'this is saturedday',
    'tuesday' : 'this is saturedday',
    'wednesday' : 'this is saturedday',
    'friday' : 'this is saturedday',
}

# def dynamic_days_by_number(request,day):
#     days_names = list(days.keys())
#     if day > len(days_names):
#         return HttpResponseNotFound("day does not exists")
#     redirect_day = days_names[day -1]
#     redirect_url = reverse('days-of-week',args=[redirect_day]) # /days-of
#     return HttpResponseRedirect(f'/days/{redirect_day}')


 
def aynamic_days(request,day):
    if day > len(days_names):
            return HttpResponseNotFound("days not exist")

    days_names = list(days.keys)
    redirect_key = days_names[day -1]
    day_data = days.get(day)
    if day_data is not None:    
         return HttpResponse(f'day is : {day} and data is : {day_data}')

    return HttpResponseNotFound("days not exist")