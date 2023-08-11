#lib
import math
print("pi is", math.pi)


#variables
nome = 10
test = "epah ya"

#conditions
if nome > 10:
    print ("nome grande")
elif nome < 10:
    print ("nome pequeno")
else:
    print ("perfeito")

#prints
print (test)
print (nome)
print (type (nome))
print (5==6)
print (5!=6)

#funcions
def print_ya():
    text = "ya"
    print(text)
    print(text)
    print(text)
    
print_ya()

def print_lol(txt):
    txt = "lol"
    
print ("babab",nome,"lala",nome)

#loops 
x=0
while(x<5):
    
    print("so mais 1 o valor e", x) 
    x=x+1
    
for x in range(5,10):
    print (x)
    
#arrays

days=["Mon", "Tue","wed","thu","fri","sat","sun"]

for d in days:
    if (d=="thu"):break
    if (d=="thu"):continue
    print(d)

