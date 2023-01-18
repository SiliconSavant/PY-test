#Program for straight line given 2 points
import math

a=float(input('x coordinate of P1: '))
b=float(input('y coordinate of P1: '))
c=float(input('x coordinate of P2: '))
d=float(input('y coordinate of P2: '))

#m=slope of line

z=(a-c)

if z==0:
    print('P1 is ',(a,b))
    print('P2 is ',(c,d))
    print('Equation of line            : x = ',a)
    print('Slope of line               : UNDEFINED')
    print('Angle made with +ive x axis : 90')
    print('X intercept                 : 0')
    print('Y intercept                 : UNDEFINED')
    exit()

m=float((b-d)/z)

if m==0:
    print('P1 is ',(a,b))
    print('P2 is ',(c,d))
    print('Equation of line            : y = ',b)
    print('Slope of line               : 0')
    print('Angle made with +ive x axis : 0')
    print('X intercept                 : UNDEFINED')
    print('Y intercept                 : 0')
    exit()

#theta is angle made with +ive x axis

theta=float((math.atan(m))*(180/math.pi))

if theta<0:
    theta=180+theta
else:
    if theta >= 180:
        theta=theta-180
    else:
        theta=theta

x_intercept=float((-b/m)+a)
y_intercept=float((-a*m)+b)


print('P1 is ',(a,b))
print('P2 is ',(c,d))
print('Equation of line            : (',y_intercept,')x + (',x_intercept,')y + (',y_intercept*x_intercept,') = 0')
print('Slope of line               : ',m)
print('Angle made with +ive x axis : ',theta)
print('X intercept                 : ',x_intercept)
print('Y intercept                 : ',y_intercept)

exit()







