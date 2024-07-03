# p10_setup_loadImage_draw_image_global
def setup():
    global imgBG,imgkitty
    size(2048,924) # 用你的background.jpg圖的大小
    imgBG= loadImage('background.jpg')
    imgkitty=loadImage('kitty.jpg')
def draw(): 
    global imgBG,imgkitty
    image(imgBG,0,0)
    image(imgkitty,mouseX,mouseY,200,230)
