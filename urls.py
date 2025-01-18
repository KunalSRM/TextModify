from django.urls import path
from django.contrib import admin
from . import views



##Video 10 Coding the backend


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('ex1',views.ex1,name='ex1')
   ## path('capfirst', views.capfirst, name='capfirst'),
   ## path('newlineremove', views.newlineremove, name='newlineremove'),
   ## path('spaceremove', views.spaceremove, name='spaceremove'),
   ## path('charcount', views.charcount, name='charcount'),
]
