import math 

num=float(input('nombre'))
print(num**(1/2), 'racine carree')


a,b,c=float(input('a')),float(input('b')), float(input('c'))
print((a+b+c)/3)


deg,minutes,sec=float(input('degrés')),float(input('minutes')),float(input('secondes'))

degr=deg+minutes/60+sec/3600
print(degr)
print(math.radians(degr))

rad=float(input('radians'))

degre=math.degrees(rad)

d=degre//1

m=(degre*60-d*60)//1

s=round((degre*3600-m*60-d*3600),0)

print(d,m,s)


far=float(input('Fahrenheit'))
cel=(far-32)/1.8
print(cel)
print(far)
