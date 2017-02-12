"""phpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from accounts import views as acc_views
from carts.views import CategoryView, CategoryDetailView

urlpatterns = [
    url(r'^$', acc_views.home_view, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', acc_views.contact_view, name="contact"),
    url(r'^login/', acc_views.login_view, name="login"),
    url(r'^logout/', acc_views.logout_view, name="logout"),

    url(r'^categories/$', CategoryView.as_view(), name="category"),
    url(r'^categories/(?P<pk>[\d]+)/$', CategoryDetailView.as_view(), name="category_detail"),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)