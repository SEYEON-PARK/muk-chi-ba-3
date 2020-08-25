class Choice():
    choice="아무거나"
class Computer():
    computer=0

def gkatn2():
     import random
     import sys
     import computer_win
     import first
     a=Choice()
     b=Computer()
     b.computer = random.randint(1,3) # 1은 가위. 2는 바위, 3은 보다.
     a.choice=input("가위, 바위, 보 중에서 하나를 입력하시오. : ")
     if(a.choice=="가위") :
       if(b.computer==1) :
           print("사용자가 이겼습니다. ")
           sys.exit()
       if(b.computer==2):
         print("컴퓨터가 바위로 이겼습니다.")
         computer_win.gkatn1()
       if(b.computer==3):
         print("사용자가 가위로 이겼습니다.(컴퓨터는 보)")
         gkatn2()
     elif(a.choice=="바위") :
       if(b.computer==2) :
           print("사용자가 이겼습니다. ")
           sys.exit()
       if(b.computer==3):
           print("컴퓨터가 보로 이겼습니다.")
           computer_win.gkatn1()
       if(b.computer==1):
           print("사용자가 바위로 이겼습니다.(컴퓨터는 가위)")
           gkatn2()
     elif(a.choice=="보") :
       if(b.computer==3) :
          print("사용자가 이겼습니다. ")
          sys.exit()
       if(b.computer==1):
          print("컴퓨터가 가위로 이겼습니다.")
          computer_win.gkatn1()
       if(b.computer==2):
          print("사용자가 보로 이겼습니다.(컴퓨터는 바위)")
          gkatn2()
     else:
         print("잘못 입력하셨습니다. 처음부터 다시 시작합니다.")
         first.main()

