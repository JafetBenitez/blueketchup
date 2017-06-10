from django.contrib import admin
from core import models

from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Profile)
admin.site.register(models.Franchise)
admin.site.register(models.Restaurant)
admin.site.register(models.Dish)

class BlueKetchupAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = BlueKetchupAdminSite()
