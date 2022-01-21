def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:    
                return float(b['balance'])
            else:
                return 0

##half-half
#def half_half(Ticker):
import time
import pyupbit
import datetime
import key
import numpy as np
import pandas as pd
flag = "KRW"



while True:
    try:
        now = datetime.datetime.now()
        access = key.access_key
        secret = key.secret_key
        upbit = pyupbit.Upbit(access, secret)

        num_count = 10
        down_ratio = 0.998
        up_ratio = 1.002

        ticker = "KRW-BTC"
        ticker_origin = "BTC"
        
        n = 0
        df = pyupbit.get_ohlcv(ticker,interval="minute3",count=num_count)
        red = df['close']-df['open']                  #양수면 빨간막대, 음수면 파란 막대


##매수 조건
        for i in list(range(0,num_count)):
            if (red[i]<0):
                n=n+1
            else:
                n=n

        if (n>=7 and (df['open'][0]*down_ratio)>=df['close'][-1] and folat(format(upbit.get_balance(ticker="KRW")))>=5000):
           print("종가가" , df['close'][-1] , "원 일때 매수 하였습니다.")
           upbit.buy_market_order(ticker,get_balance("KRW")*0.9)

        n=0
    
##매도 조건
        for i in list(range(0,num_count)):
            if (red[i]>0):
                n=n+1
            else:
                n=n

        if (n>=7 and (df['open'][0]*up_ratio)<=df['open'][-1] and float(format(upbit.get_balance(ticker="KRW-BTC")))>0):
            print("종가가" , df['close'][-1] , "원 일때 매도 하였습니다.")
            upbit.sell_market_order(ticker,get_balance(ticker_origin))
                                   
            print("보유 KRW : {}".format(upbit.get_balance(ticker="KRW")))          # 보유 KRW
            print("총매수금액 : {}".format(upbit.get_amount('ALL')))                # 총매수금액
            print("비트수량 : {}".format(upbit.get_balance(ticker="KRW-BTC")))      # 비트코인 보유수량
            time.sleep(180)
    except Exception as e:
        print(e)
        time.sleep(1)
#print("\n")
#print(upbit.get_chance('KRW-BTC')) # 마켓별 주문 가능 정보를 확인
#print("\n")
#print(upbit.get_order('KRW-XRP')) # 주문 내역 조회
