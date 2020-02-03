import sys
import requests
import json
import random
import ccxt
import pybithumb

from pandas import DataFrame
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets 
from PyQt5.QtCore import * 
from PyQt5 import uic


#from OHLC import *
#from 오더북 import *
#from 손주문 import *
#from 거래량_올리기 import *
#from 상장시 import *
#from 틱자전 import *

form_class = uic.loadUiType("MM_main.ui")[0]
#MXC 거래소 trade_type = 1: 매수, 2: 매도
#ASKS = 매도벽, BIDS = 매수벽
###############################################
access_key1 = 'c06054f79478d63bea143453d1bad71a'
secret_key1 = 'f4fadc0f01f7ba69899ca1b539e39e7b'
bithumb = pybithumb.Bithumb(access_key1, secret_key1)
trade_type1 = 'bid' #buy
trade_type2 = 'ask' #sell
###############################################
access_key = access_key1
secret_key = secret_key1
ratelimit = 0.5

class MainWindow(QtWidgets.QMainWindow, form_class): 
    def __init__(self): 
        super(MainWindow, self).__init__()
        #super().__init__()    
        self.setupUi(self)
        #OHLC
        self.pushButton_15.clicked.connect(self.create_process15) #업비트 OHLC 따라가기
        self.pushButton_30.clicked.connect(self.create_process15s) #업비트 OHLC % 따라가기        
        
        self.pushButton_1.clicked.connect(self.create_process1) #OHLC 파일 따라가기        
        self.pushButton_1ss.clicked.connect(self.create_process1ss) #OHLC 파일 % 따라가기
         
        self.pushButton_1s.clicked.connect(self.create_process1s) #오더북 따라가기
        self.pushButton_1s_2.clicked.connect(self.create_process1ss_2) #오더북 한번만      


        #오더북
        self.pushButton_2.clicked.connect(self.create_process2) #오더북 매수벽 채워넣기 버튼
        self.pushButton_3.clicked.connect(self.create_process3) #오더북 매수벽 (초) 채워넣기 버튼
        self.pushButton_4.clicked.connect(self.create_process4) #오더북 매도벽 채워넣기 버튼
        self.pushButton_5.clicked.connect(self.create_process5) #오더북 매도벽 (초) 채워넣기 버튼
        self.pushButton_66.clicked.connect(self.create_process66) #감시가격 터치 시 매수 물량 %
        self.pushButton_67.clicked.connect(self.create_process67) #감시가격 터치 시 매도 물량 %

        #손주문
        self.pushButton_6.clicked.connect(self.create_process6) #손주문 현재가 조회 버튼
        self.pushButton_7.clicked.connect(self.create_process7) #손주문 매수 버튼
        self.pushButton_8.clicked.connect(self.create_process8) #손주문 매수1 버튼
        self.pushButton_9.clicked.connect(self.create_process9) #손주문 매도 버튼    
        self.pushButton_10.clicked.connect(self.create_process10) #손주문 매도1 버튼

        self.pushButton.clicked.connect(self.create_process0) #계좌 조회 버튼
        self.pushButton_28.clicked.connect(self.create_process28) #오더 조회 버튼
        self.pushButton_29.clicked.connect(self.create_process29) #주문 취소 버튼 
        
        #거래량 올리기
        self.pushButton_11.clicked.connect(self.create_process11) #거래량 올리기 5:5 매수/매도 버튼
        self.pushButton_12.clicked.connect(self.create_process12) #거래량 올리기 매수/매도 시간 버튼
        self.pushButton_13.clicked.connect(self.create_process13) #거래량 올리기 %매수/매도 버튼
        self.pushButton_14.clicked.connect(self.create_process14) #거래량 올리기 %매수/매도 시간 버튼    

        #상장시
        self.pushButton_16.clicked.connect(self.create_process16) #상장시 매수 버튼 
        self.pushButton_17.clicked.connect(self.create_process17) #상장시 매도 버튼 
        
        #틱자전
        self.pushButton_18.clicked.connect(self.create_process18) #틱 자전1 틱 매수 버튼 
        self.pushButton_19.clicked.connect(self.create_process19) #틱 자전1 틱 매도 버튼
        self.pushButton_20.clicked.connect(self.create_process20) #틱 자전2 틱 매수 버튼 
        self.pushButton_21.clicked.connect(self.create_process21) #틱 자전2 틱 매도 버튼
        self.pushButton_22.clicked.connect(self.create_process22) #틱 자전3 틱 매수 버튼
        self.pushButton_23.clicked.connect(self.create_process23) #틱 자전3 틱 매도 버튼
        self.pushButton_24.clicked.connect(self.create_process24) #틱 자전4 틱 매수 버튼
        self.pushButton_25.clicked.connect(self.create_process25) #틱 자전4 틱 매도 버튼
        self.pushButton_26.clicked.connect(self.create_process26) #틱 자전4 틱 매수 버튼
        self.pushButton_27.clicked.connect(self.create_process27) #틱 자전4 틱 매도 버튼 

        #OHLC         
    def create_process15(self):  #업비트 OHLC 따라가기
        print("clicked-OHLC 버튼 ")
        if self.pushButton_15.text() == "OHLC ON":     
            self.pushButton_15.setText("stop process")
            
            self.process15 = OHLC3(self)  
            self.process15.start()        
        else: 
            self.process15.process15_quit_flag = True 
            print("OHLC Stop sent") 
            self.process15.wait() 
            print("OHLC Stopped") 
            self.pushButton_15.setText("OHLC ON")
            
    def create_process15s(self):  #업비트 OHLC % 따라가기
        print("clicked-OHLC 버튼 ")
        if self.pushButton_30.text() == "OHLC ON":     
            self.pushButton_30.setText("stop process")
            
            self.process30 = OHLC4(self)  
            self.process30.start()        
        else: 
            self.process30.process30_quit_flag = True 
            print("OHLC Stop sent") 
            self.process30.wait() 
            print("OHLC Stopped") 
            self.pushButton_30.setText("OHLC ON")
            
    def create_process1(self):  #OHLC 파일 따라가기
        print("clicked-OHLC 버튼 ")
        if self.pushButton_1.text() == "OHLC ON":     
            self.pushButton_1.setText("stop process")
            
            self.process1 = OHLC(self)  
            self.process1.start()        
        else: 
            self.process1.process1_quit_flag = True 
            print("OHLC Stop sent") 
            self.process1.wait() 
            print("OHLC Stopped") 
            self.pushButton_1.setText("OHLC ON") 
            
    def create_process1ss(self):  #주가 %폭 따라가기
        print("clicked-OHLC 버튼 ")
        if self.pushButton_1ss.text() == "OHLC ON":     
            self.pushButton_1ss.setText("stop process")
            
            self.process1ss = OHLC2(self)  
            self.process1ss.start()        
        else: 
            self.process1ss.process1ss_quit_flag = True 
            print("OHLC Stop sent") 
            self.process1ss.wait() 
            print("OHLC Stopped") 
            self.pushButton_1ss.setText("OHLC ON")     
            
    def create_process1s(self):  #Orderbook 따라하기
        print("clicked-Orderbook 버튼 ")
        if self.pushButton_1s.text() == "Orderbook ON":     
            self.pushButton_1s.setText("stop process")
            
            self.process1s = OHLC1(self)  
            self.process1s.start()        
        else: 
            self.process1s.process1s_quit_flag = True 
            print("OHLC Stop sent") 
            self.process1s.wait() 
            print("OHLC Stopped") 
            self.pushButton_1s.setText("Orderbook ON") 
            
    def create_process1ss_2(self):  #오더북 매수벽 채워넣기 
        print("clicked-오더북 매수벽 한번만 버튼 ")
        self.process1ss_2 = OHLC1s(self)  
        self.process1ss_2.put_ohlc1()
        
                  
        #오더북     
    def create_process2(self):  #오더북 매수벽 채워넣기 
        print("clicked-오더북 매수벽 채워넣기  버튼 ")
        self.process2 = 오더북1(self)  
        self.process2.put_buy()

    def create_process3(self):  #오더북 매수벽 채워넣기 (초 반복) 
        print("clicked-오더북 매수벽 채워넣기 (초 반복) 버튼 ")
        if self.pushButton_3.text() == "(초) 채워넣기":     
            self.pushButton_3.setText("stop process")
            
            self.process3 = 오더북2(self)  
            self.process3.start()        
        else: 
            self.process3.process3_quit_flag = True 
            print("(초) 채워넣기 Stop sent") 
            self.process3.wait() 
            print("(초) 채워넣기 Stopped") 
            self.pushButton_3.setText("(초) 채워넣기") 
        
    def create_process4(self):  #오더북 매도벽 채워넣기 
        print("clicked-오더북 매도벽 채워넣기 버튼 ")
        self.process4 = 오더북1(self)  
        self.process4.put_sell()
        
    def create_process5(self):  #오더북 매도벽 채워넣기 (초 반복)  
        print("clicked-오더북 매도벽 채워넣기 (초 반복)버튼 ")
        if self.pushButton_5.text() == "(초) 채워넣기":     
            self.pushButton_5.setText("stop process")
            self.process5 = 오더북3(self)  
            self.process5.start()        
        else: 
            self.process5.process5_quit_flag = True 
            print("(초) 채워넣기 Stop sent") 
            self.process5.wait() 
            print("(초) 채워넣기 Stopped") 
            self.pushButton_5.setText("(초) 채워넣기") 

    def create_process66(self):  #감시 가격 X 매수벽
        print("clicked-감시 가격 X 매수벽")
        if self.pushButton_66.text() == "X 매수벽":     
            self.pushButton_66.setText("stop process")
            self.process66 = 오더북4(self)  
            self.process66.start()        
        else: 
            self.process66.process66_quit_flag = True 
            print("X 매수벽 Stop sent") 
            self.process66.wait() 
            print("X 매수벽 Stopped") 
            self.pushButton_66.setText("X 매수벽") 
            
    def create_process67(self):  #감시 가격 X 매수벽
        print("clicked-감시 가격 X 매도벽")
        if self.pushButton_67.text() == "X 매도벽":     
            self.pushButton_67.setText("stop process")
            self.process67 = 오더북5(self)  
            self.process67.start()        
        else: 
            self.process67.process67_quit_flag = True 
            print("X 매도벽 Stop sent") 
            self.process67.wait() 
            print("X 매도벽 Stopped") 
            self.pushButton_67.setText("X 매도벽") 
            
        #손주문        
    def create_process6(self):  #손주문 현재가 조회 버튼 
        print("clicked-손주문 현재가 조회 버튼 ")
        self.process6 = 손주문(self)  
        self.process6.check_price()
                    
    def create_process7(self):  #손주문 매수1 버튼
        print("clicked-손주문 매수1 버튼")
        self.process7 = 손주문(self)  
        self.process7.buy1()
            
    def create_process8(self):  #손주문 매수2 버튼
        print("clicked-손주문 매수2 버튼")
        self.process8 = 손주문(self)  
        self.process8.buy2()
        
    def create_process9(self):  #손주문 매도1 버튼 
        print("clicked-손주문 매도1 버튼 ")
        self.process9 = 손주문(self)  
        self.process9.sell1()
            
    def create_process10(self):  #손주문 매도2 버튼
        print("clicked-손주문 매도2 버튼")
        self.process10 = 손주문(self)  
        self.process10.sell2()
        
    def create_process0(self): #계좌 조회
        print("clicked - 계좌 조회")
        self.process0 = 손주문(self)
        self.process0.view_account()
    
    def create_process28(self): #오더 조회
        print("clicked - 오더 조회")
        self.process0 = 손주문(self)
        self.process0.view_order()

    def create_process29(self): #주문 취소
        print("clicked - 주문 취소")    
        self.process0 = 손주문1(self)
        self.process0.cancel_order()
        
        #거래량 올리기
    def create_process11(self):  #거래량 올리기 5:5 매수/매도 버튼
        print("clicked-거래량 올리기 5:5 매수/매도 버튼")
        self.process11 = 거래량_올리기(self)  
        self.process11.five_five_buy_sell()
           
    def create_process12(self):  #거래량 올리기 매수/매도 시간 버튼
        print("clicked-거래량 올리기 매수/매도 시간 버튼 버튼")
        if self.pushButton_12.text() == "5:5 매수/매도 시간":     
            self.pushButton_12.setText("stop process")
            self.process12 = 거래량_올리기1(self)  
            self.process12.start()        
        else: 
            self.process12.process12_quit_flag = True 
            print("5:5 매수/매도 시간 Stop sent") 
            self.process12.wait() 
            print("5:5 매수/매도 시간 Stopped") 
            self.pushButton_12.setText("5:5 매수/매도 시간") 
            
    def create_process13(self): #거래량 올리기 % 매수/매도 버튼 
        print("clicked-거래량 올리기 % 매수/매도 버튼")
        self.process13 = 거래량_올리기(self)  
        self.process13.percent_buy_sell()  
        
    def create_process14(self): #거래량 올리기 % 매수/매도 버튼
        print("clicked-손주문 매도2 버튼")
        if self.pushButton_14.text() == "% 매수/매도 시간":     
            self.pushButton_14.setText("stop process")
            self.process14 = 거래량_올리기2(self)  
            self.process14.start()        
        else: 
            self.process14.process14_quit_flag = True 
            print("5:5 매수/매도 시간 Stop sent") 
            self.process14.wait() 
            print("5:5 매수/매도 시간 Stopped") 
            self.pushButton_14.setText("% 매수/매도 시간") 
        
        #상장시        
    def create_process16(self):  #상장시 매수 버튼 
        print("clicked-상장시 매수 버튼")
        self.process16 = 상장시(self)  
        self.process16.buy_list()  

    def create_process17(self):  #상장시 매도 버튼 
        print("clicked-상장시 매도 버튼")
        self.process17 = 상장시(self)  
        self.process17.sell_list()
            
        #틱 자전 코드 
    def create_process18(self):  #틱 자전1 틱 매수 
        if self.pushButton_18.text() == "틱 매수":     
            self.pushButton_18.setText("stop process")
            self.process18 = 틱자전1b(self)  
            self.process18.start()        
        else: 
            self.process18.process18_quit_flag = True 
            print("틱 자전1 매수 Stop sent") 
            self.process18.wait() 
            print("틱 자전1 매수 Stopped") 
            self.pushButton_18.setText("틱 매수")  
            
    def create_process19(self):  #틱 자전1 틱 매도 
        if self.pushButton_19.text() == "틱 매도":     
            self.pushButton_19.setText("stop process")
            self.process19 = 틱자전1s(self)  
            self.process19.start()        
        else: 
            self.process19.process19_quit_flag = True 
            print("틱 자전1 매도 Stop sent") 
            self.process19.wait() 
            print("틱 자전1 매도 Stopped") 
            self.pushButton_19.setText("틱 매도")     
      
    def create_process20(self):  #틱 자전2 틱 매수 
        if self.pushButton_20.text() == "틱 매수":     
            self.pushButton_20.setText("stop process")
            self.process20 = 틱자전2b(self)  
            self.process20.start()        
        else: 
            self.process20.process20_quit_flag = True 
            print("틱 자전2 매수 Stop sent") 
            self.process20.wait() 
            print("틱 자전2 매수 Stopped") 
            self.pushButton_20.setText("틱 매수") 
      
    def create_process21(self): #틱 자전2 틱 매도
        if self.pushButton_21.text() == "틱 매도":     
            self.pushButton_21.setText("stop process")
            self.process21 = 틱자전2s(self)  
            self.process21.start()        
        else: 
            self.process21.process21_quit_flag = True 
            print("틱 자전2 매도 Stop sent") 
            self.process21.wait() 
            print("틱 자전2 매도 Stopped") 
            self.pushButton_21.setText("틱 매도") 
    
    def create_process22(self):  #틱 자전3 틱 매수 
        if self.pushButton_22.text() == "틱 매수":     
            self.pushButton_22.setText("stop process")
            self.process22 = 틱자전3b(self)  
            self.process22.start()        
        else: 
            self.process22.process22_quit_flag = True 
            print("틱 자전3 매수 Stop sent") 
            self.process22.wait() 
            print("틱 자전3 매수 Stopped") 
            self.pushButton_22.setText("틱 매수") 
    
    def create_process23(self):  #틱 자전3 틱 매도 
        if self.pushButton_23.text() == "틱 매도":     
            self.pushButton_23.setText("stop process")
            self.process23 = 틱자전3s(self)  
            self.process23.start()        
        else: 
            self.process23.process23_quit_flag = True 
            print("틱 자전3 매도 Stop sent") 
            self.process23.wait() 
            print("틱 자전3 매도 Stopped") 
            self.pushButton_23.setText("틱 매도") 
      
    def create_process24(self):  #틱 자전4 틱 매수 
        if self.pushButton_24.text() == "틱 매수":     
            self.pushButton_24.setText("stop process")
            self.process24 = 틱자전4b(self)  
            self.process24.start()        
        else: 
            self.process24.process24_quit_flag = True 
            print("틱 자전4 매수 Stop sent") 
            self.process24.wait() 
            print("틱 자전4 매수 Stopped") 
            self.pushButton_24.setText("틱 매수") 
      
    def create_process25(self): #틱 자전4 틱 매도
        if self.pushButton_25.text() == "틱 매도":     
            self.pushButton_25.setText("stop process")
            self.process25 = 틱자전4s(self)  
            self.process25.start()        
        else: 
            self.process25.process25_quit_flag = True 
            print("틱 자전4 매도 Stop sent") 
            self.process25.wait() 
            print("틱 자전4 매도 Stopped") 
            self.pushButton_25.setText("틱 매도") 
    def create_process26(self): #틱 자전4 틱 매수
        if self.pushButton_26.text() == "틱 매수":     
            self.pushButton_26.setText("stop process")
            self.process26 = 틱자전5b(self)  
            self.process26.start()        
        else: 
            self.process26.process26_quit_flag = True 
            print("틱 자전5 매수 Stop sent") 
            self.process26.wait() 
            print("틱 자전5 매수 Stopped") 
            self.pushButton_26.setText("틱 매수") 
    def create_process27(self): #틱 자전4 틱 매도
        if self.pushButton_27.text() == "틱 매도":     
            self.pushButton_27.setText("stop process")
            self.process27 = 틱자전5s(self)  
            self.process27.start()        
        else: 
            self.process27.process27_quit_flag = True 
            print("틱 자전5 매도 Stop sent") 
            self.process27.wait() 
            print("틱 자전5 매도 Stopped") 
            self.pushButton_27.setText("틱 매도") 
    
if __name__=="__main__": 
    app=QtWidgets.QApplication(sys.argv) 
    ex = MainWindow() 
    ex.show() 
    sys.exit(app.exec_()) 