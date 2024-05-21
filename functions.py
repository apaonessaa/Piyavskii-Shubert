import math  
##################################### Function ####################################  
# fX = lambda function  
# tX = (a,b,L) 

f0 = lambda x : 1
t0 = (-1,1,0.5)

f1 = lambda x : (1/6)*x**6-(52/25)*x**5+(39/80)*x**4+(71/10)*x**3-(79/20)*x**2-x+(1/10)
t1=(-1.5,11,13870)

f2 = lambda x : math.sin(x)+math.sin(10*x/3)
t2=(2.7,7.5,4.29)

def f3(x):
    k = 1
    ris = 0
    while k <= 5:
        ris += k*math.sin((k+1)*x+k)
        k += 1
    return -ris
t3=(-10,10,67)

f4 = lambda x : -(16*x**2-24*x+5)*math.exp(-x)
t4=(1.9,3.9,3)

f5 = lambda x : (3*x-1.4)*math.sin(18*x)
t5=(0,1.2,36)

f6 = lambda x : -(x+math.sin(x))*math.exp(-(x**2))
t6=(-10,10,2.5)

f7 = lambda x : math.sin(x)+math.sin(10*x/3)+math.log(x)-0.84*x+3
t7=(2.7,7.5,6)

def f8(x):
    k = 1
    ris = 0
    while k <= 5:
        ris += k*math.cos((k+1)*x+k)
        k += 1
    return -ris
t8=(-10,10,67)

f9 = lambda x : math.sin(x)+math.sin(2*x/3)
t9=(3.1,20.4,1.7)

f10 = lambda x : -x*math.sin(x)
t10=(0,10,11)

f11 = lambda x : 2*math.cos(x)+math.cos(2*x)
t11=(-1.57,6.28,3)

f12 = lambda x : (math.sin(x))**3+(math.cos(x))**3
t12=(0,6.28,2.2)

f13 = lambda x : -(x**(2/3))+math.cbrt(x**2-1) 
t13=(0.001,0.99,8.5)

f14 = lambda x : -math.exp(-x)*math.sin(2*math.pi*x)
t14=(0,4,6.5)

f15 = lambda x : (x**2-5*x+6)/(x**2+1)
t15=(-5,5,6.5)

f16 = lambda x : 2*(x-3)**2+math.exp(1)**(0.5*x**2)
t16=(-3,3,85)

f17 = lambda x : x**6-15*x**4+27*x**2+250
t17=(-4, 4, 2520)

f18 = lambda x : (x-2)**2 if x<=3 else 2*math.log(x-2)+1
t18=(0,6,4)

f19 = lambda x : -x+math.sin(3*x)-1
t19=(0, 6.5, 4)

f20=lambda x : (math.sin(x)-x)*math.exp(-(x**2))
t20=(-10, 10, 1.3)