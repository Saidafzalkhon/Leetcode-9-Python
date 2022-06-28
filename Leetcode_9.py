x = int(input())
mantiq = False
if x<0:
    print(mantiq)
elif x < 10:  
    mantiq = True
    print(mantiq)
else:
    harfga = str(x)
    uzunlik = int(len(harfga))
    for i in range(len(harfga)//2):
        uzunlik-=1
        mantiq = False
        if harfga[i] == harfga[uzunlik]:
            mantiq = True
        else: 
              mantiq = False
              break
        
    print(mantiq)
