doors  = [False]*100
x = []

for index,door in enumerate(doors):
    #print("index glowny" + str(index))

    for index2 in range(0,99, index+1):
        #print (str (index),str (index2))
        if doors [index2] == False:
            doors [index2] = True
        else:
            doors [index2] = False

for index,door in enumerate(doors):
    if door is True:
    	x.append(index)

print("The following doors are open:",(x))