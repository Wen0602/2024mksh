# p12_for_many_image_list_void_mousePressed
def setup():
    global imgBG,imgkitty
    size(2048,924) # 用你的background.jpg圖的大小
    imgBG= loadImage('background.jpg')
    imgkitty=loadImage('kitty.jpg')
def draw(): 
    global imgBG,imgkitty
    image(imgBG,0,0)
    for i in range(10):
        image(imgkitty,x[i],y[i],200,230)
    image(imgkitty,mouseX,mouseY,200,230)
x = [0]*10
y = [0]*10
N = 0    
def mousePressed():
    global N
    x[N], y[N] = mouseX,mouseY
    N += 1
