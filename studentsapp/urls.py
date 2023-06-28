"""studentsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("notes/",views.notes,name="notes"),
    path("notes/remove/<int:pk>",views.delete_notes,name="delete-notes"),
    path("notes/detail/<int:pk>",views.NotesDetailsView.as_view(),name='notes-details'),

    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete-homework'),
    path('youtube',views.youtube,name='youtube'),
]
