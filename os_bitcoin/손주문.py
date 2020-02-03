from PyQt5 import QtWidgets 
from PyQt5.QtCore import * 
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
import sys 
import time 
import random
import threading
import pybithumb
form_class = uic.loadUiType("MM_main.ui")[0]
#MXC 거래소 trade_type = 1: 매수, 2: 매도
#ASKS = 매도벽, BIDS = 매수벽
###############################################
access_key1 = 'c06054f79478d63bea143453d1bad71a'
secret_key1 = 'f4fadc0f01f7ba69899ca1b539e39e7b'
bithumb = pybithumb.Bithumb(access_key1, secret_key1)
symbol1 = 'ABT/KRW'
###############################################
access_key = access_key1
secret_key = secret_key1
ratelimit = 0.5

class 손주문(QThread):  #틱자전1 매수
    def __init__(self, parent): 
        super(손주문, self).__init__(parent)  
        self.symbol_str = self.parent().lineEdit_93.text() #코인 이름 입력 값
        self.price =  self.parent().lineEdit_69.text() #현재가가 나옵니다 값
        self.tick = self.parent().lineEdit_126.text() #틱 단위 값           
        self.price_buy1 = self.parent().lineEdit_87.text() #매수 가격1 값
        self.quantity_buy1 = self.parent().lineEdit_83.text() #매수 수량1 값
        self.price_buy2 = self.parent().lineEdit_86.text() #매수 가격2 값
        self.quantity_buy2 = self.parent().lineEdit_84.text() #매수 가격2 값
        
        self.price_sell1 = self.parent().lineEdit_62.text() #매도 가격1 값
        self.quantity_sell1 = self.parent().lineEdit_85.text() #매도 수량1 값
        self.price_sell2 = self.parent().lineEdit_65.text() #매도 가격2 값
        self.quantity_sell2 = self.parent().lineEdit_88.text() #매도 가격2 값
        
    def check_price(self):
        a= (bithumb.get_current_price(self.symbol_str))
        last = str(a)
        self.parent().lineEdit_69.setText(last)
        print(self.price)
        
    def buy1(self):
        tick = float(self.tick)
        symbol = self.symbol_str
        price = float(self.price_buy1)
        if(float(tick)==1 or float(tick)==10 or float(tick)==100):
            price = int(float(price))
        count = float(self.quantity_buy1)
        print("매수1 주문", {'symbol':symbol,'price':price,'count':count})
        print(bithumb.buy_limit_order(symbol,price,count))
        
    def buy2(self):
        tick = float(self.tick)
        symbol = self.symbol_str
        price = float(self.price_buy2)
        if(float(tick)==1 or float(tick)==10 or float(tick)==100):
            price = int(float(price))
        count = float(self.quantity_buy2)
        print("매수2 주문", {'symbol':symbol,'price':price,'count':count})
        print(bithumb.buy_limit_order(symbol,price,count)) 
        
    def sell1(self):
        tick = float(self.tick)
        symbol = self.symbol_str
        price = float(self.price_sell1)
        if(float(tick)==1 or float(tick)==10 or float(tick)==100):
            price = int(float(price))
        count = float(self.quantity_sell1)
        print("매도1 주문", {'symbol':symbol,'price':price,'count':count})
        print(bithumb.sell_limit_order(symbol,price,count))
        
    def sell2(self):
        tick = float(self.tick)
        symbol = self.symbol_str
        price = float(self.price_sell2)
        if(float(tick)==1 or float(tick)==10 or float(tick)==100):
            price = int(float(price))
        count = float(self.quantity_sell2)
        print("매도2 주문", {'symbol':symbol,'price':price,'count':count})
        print(bithumb.sell_limit_order(symbol,price,count))  

    def view_account(self): #계정 조회
        for coin in bithumb.get_tickers():
            print(coin, bithumb.get_balance(coin))  

    def view_order(self): #오더 조회
        print(bithumb.get_outstanding_order('bid'))
        print(bithumb.get_outstanding_order('ask'))        

class 손주문1(QThread):  #틱자전1 매수
    def __init__(self, parent): 
        super(손주문1, self).__init__(parent)  
        self.order_id = self.parent().lineEdit_108.text()  
        
    def cancel_order(self): #주문 취소
        status = bithumb.cancel_order(self.order_id)    
        
