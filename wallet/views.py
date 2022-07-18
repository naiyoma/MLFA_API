from django.shortcuts import render
from .serializers import WalletSerializer, DepositSerializer, WithdrawSerializer, TransferSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .models import Transfer, Wallet, Deposit, Withdraw, Transfer
# Create your views here.

class UserWalletCreate(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class DepositCreate(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class WithdrawCreate(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

class TransferCreate(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer




