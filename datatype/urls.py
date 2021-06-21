from django.urls import path
from .views import home_view, covid_chart, test, prolang, anime_chart, ide_chart, website_chart, database

urlpatterns = [
    path('home/', home_view, name="home"),
    path('covid_chart/', covid_chart, name="covid-chart"),
    path('test', test, name='test'),
    path('ide/', ide_chart, name='ide-chart'),
    path('wesite/', website_chart, name='website-chart'),
    path('anime/', anime_chart, name='anime-chart'),
    #path('population-chart/', bar_test, name='population-chart'),
    path('prolan/', prolang, name='prolang-chart'),
    path('database/', database, name='db-chart')
]