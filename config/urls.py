"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import exam.urls
from exam.views import (
    NotebookListAPIView,
    NotebookDeleteAPIView,
    NotebookCreateAPIView,
    NotebookDetailAPIView,
    NotebookUpdateAPIView,
    NotebookDeleteUpdateDetailAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', NotebookListAPIView.as_view(), name='notebook-list'),
    path('delete/<int:pk>/', NotebookDeleteAPIView.as_view(), name='notebook-delete'),
    path('create/', NotebookCreateAPIView.as_view(), name='notebook-create'),
    path('detail/<int:pk>/', NotebookDetailAPIView.as_view(), name='notebook-detail'),
    path('update/<int:pk>/', NotebookUpdateAPIView.as_view(), name='notebook-update'),
    path('item/<int:pk>/', NotebookDeleteUpdateDetailAPIView.as_view(), name='notebook-item'),
]
