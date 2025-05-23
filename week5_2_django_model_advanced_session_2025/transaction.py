from django.db import transaction
from django.shortcuts import render

# Create your views here.

# Transation 예제
# 국민 은행 계좌를 가지고 있는 A가 우리 은행의 계좌를 가지고 있는 B에게 1만원을 송금하는 상황을 가정
#
# 아래	와 같은 과정을 나열해볼 수  있습니다.
# 1. 국민 은행에서 A의 계좌 금액을 조회한다.
# 2. A 계좌의 금액이 1만원보다 많은지 확인하고, 1만원을 차감한다.
# 3. 국민 은행에서 우리 은행으로 1만원을 보낸다.
# 4. 우리 은행에서 B의 계좌를 조회한다.
# 5. 우리 은행에서 B의 계좌에 1만원을 추가한다.

class AccountBalanceError(Exception):
    """잔액 부족 예외 처리 클래스"""
    pass

def get_account_info(bank, account):
    pass


# @transaction.atomic()
def 송금(request):
    # 1. 국민 은행에서 A의 계좌 금액을 조회한다.
    A_account = get_account_info('국민은행', 'A')

    # 2. A 계좌의 금액이 1만원보다 많은지 확인하고, 1만원을 차감한다.
    A_balance = A_account.get_balance() # A 계좌의 잔액 조회
    if A_balance < 10000:
        raise AccountBalanceError("잔액이 부족합니다.") # 잔액 부족 예외 처리

    with transaction.atomic():
        A_account.withdraw(10000) # A 계좌에서 1만원 차감 -> 데이터베이스에 데이터 변경이 일어남

        # 3. 국민 은행에서 우리 은행으로 1만원을 보낸다.
        A_account.transfer('우리은행', 10000) # A 계좌에서 우리은행 B 계좌로 1만원 송금  -> 데이터베이스에 데이터 변경이 일어남

        # 4. 우리 은행에서 B의 계좌를 조회한다.
        B_account = get_account_info('우리은행', 'B')

        # 5. 우리 은행에서 B의 계좌에 1만원을 추가한다.
        B_account.deposit(10000) # B 계좌에 1만원 추가  -> 데이터베이스에 데이터 변경이 일어남



