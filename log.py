#-*-coding:utf8;-*- 
#qpy:console

def rang(start, stop, step): 
    start = float(start) 
    stop = float(stop) 
    step = float(step) 
    array = []
    while start < stop:                                                   
        array.append(round(start, 4)) 
        start += step       
    return array
base = float(input("Enter the base of the logarithm table: ")) 
#print(rang(0,100,0.1)) 
                            
#for z in range(1,100):
for y in rang(0,2,0.0001):
    x = base**y
    #if  z == round(x, 1) :
    print("Log of", x, "is:" , y) 
