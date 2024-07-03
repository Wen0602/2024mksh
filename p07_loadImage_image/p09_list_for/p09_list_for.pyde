# p09_list_for
names=['Alice','Amy','Tom'] # list陣列
for name in names:
    print(name)
background(138,166,240)    
size(300,300)  
for i in range(len(names)):
    text(names[i],i*100,100)
