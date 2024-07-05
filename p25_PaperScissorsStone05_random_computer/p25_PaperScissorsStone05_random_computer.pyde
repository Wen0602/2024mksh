# p25_PaperScissorsStone05_random_computer
import random
select,computer = -1,-1
def setup():
    size(600,300)
    
def draw():
   
    fill (250,151,163)#白色的格子
    rect(0,0,300,300)
    
    rect(300,0,300,300) 
    
     
    for i in range(3):
        if computer==i: fill(161,181,252)
        else:fill(255)
        rect(100,100+i*50,100,50)
   
    for i in range(3):
        if select==i: fill(161,181,252)
        else:fill(255)
        rect(400,100+i*50,100,50)    
    
    textSize(25)#文字大小
    textAlign(LEFT,TOP)#對齊左上
    fill(0)#黑色字
    for i in range(2):
        text("Paper",100+i*300,100)
        text("Scissor",100+i*300,150)
        text("Stone",100+i*300,200)
def mousePressed(): #如果mouse按下去
    global select,computer
    if 400<mouseX<400+100:# 左右在範圍內
        if 100<mouseY<150: select=0
        if 150<mouseY<200: select=1
        if 200<mouseY<250: select=2
    computer = int(random.randrange(3))   
    
    if select==computer:
        print("tie")
    elif select==0 and computer==1:
        print("you win")
        fill(0)
    elif select==1 and computer==2:
        print("you win")
        fill(0)
    elif select==2 and computer==0:
        print("you win") 
        fill(0)
    else: #沒平手,也沒贏 那就是輸了
        print("you lose")   
    
