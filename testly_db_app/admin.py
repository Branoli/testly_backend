from django.contrib import admin
from testly_db_app.models import WoodTable
from mptt.admin import MPTTModelAdmin

admin.site.register(WoodTable, MPTTModelAdmin)