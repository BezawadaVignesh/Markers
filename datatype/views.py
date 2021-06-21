from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .myapi import get_timeline, get_country
from .forms import ConactForm
from django.contrib import messages
from .models import Message

timeline_data = []
country_data = []

def func1():
    global timeline_data
    if timeline_data == []:
        timeline_data = get_timeline()
    return timeline_data

def func2():
    global country_data
    if country_data == []:
        country_data = get_country()
    return country_data

info = func1()
cinfo = func2()

def get_from_data(want):
    return info[0][want]
# Create your views here.
def covid_chart(request, *args, **kwargs):    
    pie_labels = ["recovered", "deaths", "active"]
    pie_data = []
    for want in pie_labels:
        pie_data.append(get_from_data(want)/1000000)
    list = [13,38,48,76,80,96,110,159,175,178,213]
    bar_data =[]
    for i in list:
        bar_data.append(cinfo[i]['latest_data']['confirmed']/1000000)
    bar_labels = ['Bangladesh','Brazil','China','Germany','France','India','Italy','Russia','Turkey','Spain','USA']
    '''
    bar_data, bar_labels = pie_data, pie_labels
    line_data0 =[]
    line_data1 = []
    line_labels=[]
    line_data=[]
    num=0
    for i in range(30):
        line_labels.append(info[i]['date'])
        line_data0.append(info[i]['confirmed'])
        line_data1.append(info[i]['recovered'])

        if num==20:
            break
        num += 1

    line_data.append(line_data0[::-1])
    line_data.append(line_data1[::-1])'''
    updated = info[0]['updated_at'][:10] + " Time: " +info[0]['updated_at'][12:20]
    return render(request, "covid.html", {
        'pie_labels': pie_labels,
        'pie_data': pie_data,
        'bar_labels': bar_labels,
        'bar_data':bar_data,
        'total_confirmed':info[i]['confirmed'],
        'updated_time': updated,
        })
    #return HttpResponse("<h1>Home</h1>")

def home_view(request):
    form = ConactForm()
    if request.method == 'POST':
        form = ConactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            sender_email = form.cleaned_data['sender_email']
            message = form.cleaned_data['message']
            msg = Message(sender=sender, sender_email=sender_email, message=message)
            msg.save()
            print(sender," -->", sender_email," -->", message)
            messages.success(request, "Message sent successfully.. ")
    return render(request, 'Home.html', {'form': form})

def test(request):
    return JsonResponse({"data":{"1":"This is data"}})

def anime_chart(request):
    return render(request, 'anime.html')

def database(request):
    return render(request, 'database.html')

def website_chart(request):
    return render(request, 'website.html')

def ide_chart(request):
    return render(request, 'IDE.html')

def prolang(request):
    labels=["Java","C/C++","PHP","Python","JavaScript","C#","TypeScript","Kotlin","Go","Visual Basic"]
    data = [22.23, 8.12, 6.89, 30.35, 10.17, 6.83, 2.04,1.87,0.77,0.43]
    return render(request, 'prolang.html', {"bar_labels":labels,'bar_data':data} )