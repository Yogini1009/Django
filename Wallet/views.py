# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import routers, viewsets
from .models import Profile, Account , Mwallet ,Transaction
from .serializers import ProfileSerializer, AccountSerializer ,MwalletSerializer, TransactionSerializer
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import DepositForm, TransactionForm
from .import models
    
    
    

class Meta:
        pass

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user = user)

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # def create(self, validated_data):
    #     profile     = get_object_or_404(Profile, user = self.request.user)
    #     mwallet     = Mwallet.objects.get(wallet_id = profile)
    #     dmwallet    = Mwallet.objects.get(wallet_id = transaction.to_id)
    #     if mwallet.balance >= self.amount:
    #         mwallet.balance    -= self.amount
    #         dmwallet.balance   += self.amount
    #         self.status  = "Sucessful"
    #     else:
    #         self.status = "Failed"
    #         mwallet.save()
    #         dmwallet.save()
    #     return self.save()

class MwalletViewSet(viewsets.ModelViewSet):
     queryset = Mwallet.objects.all()
     serializer_class = MwalletSerializer


@login_required()
def diposit_view(request):
    title = "Deposit"
    deposited_amt = 0
    form = DepositForm(request.POST or None)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            deposit = form.save(commit=False)
            # adds users deposit to balance.
            profile = Profile.objects.get(user=user)
            mwallet = Mwallet.objects.get(wallet_id = profile)
            mwallet.balance += deposit.amount
            profile.account.balance -= deposit.amount
            deposited_amt = deposit.amount
            mwallet.save()
            profile.account.save()
            deposit.user = user
            deposit.save()

    context = {
                "user": user,
                "title": title,
                "deposited_amt": deposited_amt,
                "form": form
              }
    return render(request, "form.html", context)

@login_required()
def transaction_view(request):
    title = "Transaction"
    form = TransactionForm(request.POST or None)
    profile = get_object_or_404(Profile, user = request.user)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            mwallet     = Mwallet.objects.get(wallet_id = profile)
            dmwallet    = Mwallet.objects.get(wallet_id = transaction.to_id)
            if mwallet.balance >= transaction.amount:
                mwallet.balance    -= transaction.amount
                dmwallet.balance   += transaction.amount
                transaction_amt     = transaction.amount
                transaction.status  = "Sucessful"
            else:
                transaction.status = "Failed"
            mwallet.save()
            dmwallet.save()
            transaction.from_id=profile
            # transaction.user = profile
            transaction.save()

    context = {
                 "user": profile,
                 "title": title,
                 "form": form
               }

       
    return render(request, "form.html", context)
     #   return redirect("login.html")
    #else:
     #   form = forms.TransactionForm()
    #return render(request, "money_transfer.html", {"form": form})


router = routers.DefaultRouter()

router.register('profile', ProfileViewSet, base_name="profile-list")
router.register('account', AccountViewSet, base_name="account-list")
router.register('transactions', TransactionViewSet, base_name="transaction-list")
router.register('Mwallet', MwalletViewSet, base_name="mwallet-list")
