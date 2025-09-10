from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from projectvm.views import account_dashboard
from django.shortcuts import redirect


def redirect_to_dashboard(request):
    return redirect('account_dashboard')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectvm.urls')),  # Routes to app-level urls.py

]
handler404 = "internship.views.handler404"
handler500 = "internship.views.handler500"
handler403 = "internship.views.handler403"
handler400 = "internship.views.handler400"
