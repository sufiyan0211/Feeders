
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('sports/',views.sports,name='sports'),
    path('covid/',views.covid,name='covid'),
    path('news/',views.news,name='news'),
    path('business/',views.business,name='business'),
    path('technology/',views.technology,name='technology'),
    path('educations/',views.educations,name='educations'),
    path('fasion/',views.fasion,name='fasion'),
    path('movies/',views.movies,name='movies'),
    path('series/',views.series,name='series'),
    

]



urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)