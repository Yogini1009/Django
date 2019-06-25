from django import forms
from .models import Diposit
from .models import Transaction


class DepositForm(forms.ModelForm):
    class Meta:
        model = Diposit
        fields = ["amount"]



class TransactionForm(forms.ModelForm):    
    class Meta:
        model = Transaction
        fields = ["to_id" , "amount", "status"]
    