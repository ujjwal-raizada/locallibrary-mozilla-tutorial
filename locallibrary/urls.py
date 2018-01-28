"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

# use include() to add paths from the calalog application
from django.urls import include

urlpatterns += [

	path('catalog/',include('catalog.urls')),

]

# add URL maps to redirect the base URL to our application

from django.views.generic import RedirectView

urlpatterns += [

	path('',RedirectView.as_view(url='/catalog/')),
]

"""

Leave the first parameter of the path function empty to imply '/'. If you write the first parameter as '/' Django will give you the following warning when you start the development server:

System check identified some issues:

WARNINGS:
?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'. 
Remove this slash as it is unnecessary. 
If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.

"""


# use static() to add url mapping to serve static files during development (only) (WHY?)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# import statements are used just before their requirements for better understanding
# but in common practice they are written at the top of the code

































