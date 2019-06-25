# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator
from django import forms
from decimal import Decimal

# Create your models here.
class Account(models.Model):
    account = models.CharField(max_length=11,default='')
    atype   = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2,
      max_digits=12,
      validators=[
          MinValueValidator(Decimal('10.00'))
          ])
    branch  = models.CharField(max_length=5)

    class Meta:
        pass

    def __str__(self):
        return self.account

class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    account     = models.OneToOneField(Account, on_delete=models.CASCADE)
    phone       = models.CharField(max_length=10)
   

    class Meta:
        pass

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


    


class Mwallet(models.Model):
    wallet_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    balance   = models.DecimalField(decimal_places=2,
      max_digits=12,
      )
    class Meta:
        pass

    def __str__(self):
        return self.wallet_id.user.first_name


statusChoices = (
  ('Pending', 'Pending'),
  ('Sucessful', 'Sucessful'),
  ('Failed', 'Failed'),
)

class Transaction(models.Model):
    from_id    = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="sender")
    to_id      = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="receiver")
    amount     = models.DecimalField(decimal_places=2,max_digits=12)
    status     = models.CharField(max_length=15, choices = statusChoices)
    timestamp  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        pass

    def __str__(self):
        return str(self.to_id) + " " + str(self.amount)

    def save(self, *args, **kwargs):
      statusoptions = dict(statusChoices)
      # self.status = statusoptions['Pending']
      super(Transaction,self).save()

class Diposit(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('10.00'))])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)





