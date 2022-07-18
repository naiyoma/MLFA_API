from django.urls import path
from .views import UserWalletCreate, DepositCreate, WithdrawCreate, TransferCreate


app_name='wallet'

urlpatterns = [
    path('create', UserWalletCreate.as_view()),
    path('deposit', DepositCreate.as_view()),
    path('withdraw', WithdrawCreate.as_view()),
    path('transfer', TransferCreate.as_view())
]

