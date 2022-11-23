print("0       = MOHAMED EL KATI EL YMLAHI =  ")
for i in range(1,10):
    for j in range(1,i):
        print("*" , end="")
    print()
print("1       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,10):
    for j in range(1,10-i):
        print("*" , end="")
    print()
print("2       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,9):
    for j in range(1,19):
        print("*" , end="")
    print()
print("3       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,11):
    print((10-i)*" " ,((i*2)-1)*"*" , end=""  )
    print()

print("4       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,11):
    print((i-1)*" " , (((11-i)*2)-1)*"*" , end="" )
    print()
print("5       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1 , 10):
    print((10 - i) * "  ",  end="")
    for j in range(0, ((i*2)-1)):
        print(" *", end="")
    print()

print("6       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1, 10):
    print((i - 1) * "  " , end="")
    for j in range(0, (((10-i)*2)-1)):
        print(" *", end="")
    print()
print("7       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,10):
    print((10 - i) *2* " ", ((i * 2) - 1) * " *", (10 - i) * " ", end="")
    print()
for i in range(1,9):
    print((i+1 ) *2* " ", (((9 - i) * 2) - 1) * " *", end="")
    print()
print("8       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,19):
    if i < 10 :
        print((10 - i) *2* " " , end="")
        for j in range(0,((i * 2) - 1)):
            print(" *", end="")
        print()
    else:
        print((i-9 ) *2* " ", end="")
        for j in range(0,(((19 - i) * 2) - 1)):
                print(" *", end="")
        print()
print("9       = MOHAMED EL KATI EL YMLAHI =  ")
#
for i in range(1,9):
    t=((9 - i) * 2) - 1
    if t>1:
        print((i+1 )* " ", " *",(((10 - i)*2)-6) * " ", " *", end="")
        print()
    else:
        print((i + 2) * " ", " *", end="")
        print()
for i in range(1,10):
    y=((i * 2) - 1)
    if y>1:
        print((10 - i) * " "," *",(((i+1 ) *2)-6)* " "," *", end="")
        print()
print("10       = MOHAMED EL KATI EL YMLAHI =  ")
#
a = 0
b = 18
for t in range (1,19):
    for y in range (1,19):
        if y==a or y==b :
            print("*", end=" ")
        else:
            print(" ", end=" " )
    print()
    a=a+1
    b=b-1
