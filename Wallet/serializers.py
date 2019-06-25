from rest_framework import serializers
from .models import Profile, Account, Mwallet , Transaction ,Diposit

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'account','phone')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account 
        fields = ('account','atype','balance','branch')

class MwalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mwallet 
        fields = ('wallet_id', 'balance')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ( 'from_id', 'to_id', 'amount', 'status', 'timestamp')
 
class DipositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diposit
        fields = ('user', 'amount', 'timestamp')
