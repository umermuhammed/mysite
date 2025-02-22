"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp2 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form,name="login"),
    path('home/', views.home,name="signup"),
    path('save_order/', views.save_order, name='save_order'),
    path('survey/', views.survey, name='survey'),
    path('survey/<int:pk>/<str:choice>', views.updateSurvey, name='update-survey'),

    path('clear_table/', views.clear_table, name='clear_table'),
    path('filter-table/<str:category>/', views.filter_table, name='filter_table'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
