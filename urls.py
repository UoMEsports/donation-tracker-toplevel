from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy

import tracker.views

# Set custom headers for admin site based on site name in settings.
admin.AdminSite.site_title = ugettext_lazy('{} site admin'.format(settings.SITE_NAME))
admin.AdminSite.site_header = ugettext_lazy('{} administration'.format(settings.SITE_NAME))

urlpatterns = [
    path('', include('tracker.urls')),
    path('admin/lookups/', include('ajax_select.urls')),
    path('admin/', admin.site.urls),
    path('logout', tracker.views.logout),
]
