# p11_for_many_image
def setup():
    global imgBG,imgkitty
    size(2048,924) # 用你的background.jpg圖的大小
    imgBG= loadImage('background.jpg')
    imgkitty=loadImage('kitty.jpg')
def draw(): 
    global imgBG,imgkitty
    image(imgBG,0,0)
    for i in range(10):
        image(imgkitty,i*200,0,200,230)
    image(imgkitty,mouseX,mouseY,200,230)
