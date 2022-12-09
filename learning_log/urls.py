"""learning_log URL Configuration

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
from django.urls import path, include
# The first two lines import functions and modules that
# manage project URLs and the administrative site

# The urlpatterns variable is defined in the file body
urlpatterns = [
    # The code includes the admin.site.urls module, which defines all URLs that can be requested from the administrative site
    path('admin/', admin.site.urls),

    # This string will match any URL that starts with the word users
    path('users/', include('users.urls')),

    # A line is added to enable the learning_logs.urls module
    path('', include('learning_logs.urls')),
]
