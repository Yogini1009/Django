# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Profile
from.models import Account
from.models import Mwallet
from.models import Diposit,Transaction

admin.site.register(Profile)
admin.site.register(Account)
admin.site.register(Mwallet)
admin.site.register(Diposit)
admin.site.register(Transaction)
