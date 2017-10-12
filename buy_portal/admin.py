# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item,Requirement,Advertisement

# Register your models here.
admin.site.register(Item)
admin.site.register(Advertisement)
admin.site.register(Requirement)