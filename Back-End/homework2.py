# home work1

# d=int(input('diametri daxil edin'))
# r=d/2
# p=3
# s=p*r**2

# print(s)

# home work2

# deyisken=""" Sweep through the days Like children that can't stay awake """ 
# print(len(deyisken))
# deyer=int(input('reqem daxil edin'))
# print(deyisken[:deyer])
# if(deyer>len(deyisken)):
#     print('boyuk reqem daxil etdiniz')
# elif (deyer<0):
#     print('false')

    
# home work3

# ad=input('adinizi daxil edin')
# soyad=input('soyadinizi daxil edin')
# mail=ad+soyad+"@gmail.com"
# print(mail)

# home work4

# x=int(input('birinci reqem'))
# y=int(input('ikinci reqem'))
# emel=input('istifade etmek isdeyiniz emel:+ ,- ,*,/')

# if(emel=='+' and emel=='-' and emel=='*' and emel=='/'):
#     print('zehmet olmasa yazilan emellerden birin secin')
# elif(emel=='+'):
#     cavab=x+y
#     print(f'riyazi emel: {emel}  :  {x}+{y}={cavab}')
# elif(emel=='-'):
#     cavab=x-y
#     print(f'riyazi emel: {emel}  :  {x}-{y}={cavab}')
# elif(emel=='/'):
#     cavab=x/y
#     print(f'riyazi emel: {emel}  :  {x}/{y}={cavab}')
# elif(emel=='*'):
#     cavab=x*y
#     print(f'riyazi emel: {emel}  :  {x}*{y}={cavab}')
# else:
#     print('false')

# home work5

# n=int(input('eded daxil edin'))

# if(n % 2==0):
#     print("CUT")
# else:
#     print("TEK")

#home work 6

# n=int(input("reqem daxil edin"))
# a=int(input('reqem daxil edin'))
# b=int(input('reqem daxil edin'))

# if(n % a ==0 and n % b ==0):
#     print('yes')
# else:
#     print('no')

#home work7

# n=int(input('tam eded daxil edin'))

# if(n>0):
#     print('Positive')
# elif(n<0):
#     print('Negative')
# elif(n==0):
#     print('Zero')

#home work8
# print('ucbucagin tereflerin girin')
# a=int(input("a: daxil edin"))
# b=int(input('b: daxil edin'))
# c=int(input('c: daxil edin'))

# if(a + b > c and b + c > a and a + c>b):
#     print("yes")
#     if(a==b and a==c and c==b):
#         print('beraber terefli ucbucaq')
#     elif((a*a + b*b) == c*c or b**2 + c**2 == a**2 or a**2 + c**2 == b**2):
#         print('duzbucaqli ucbucaq')
#     else:
#         print('muxtelif terefli ucbucaq')
# else:
#     print('no')

#home work9

# bal=int(input('balnizi qeyd edin'))

# if(1<=bal<=12):
#     if(1<=bal<=3):
#         print('Initial')
#     elif(3<bal<=6):
#         print('Average')
#     elif(6<bal<=9):
#         print('Sufficient')
#     elif(9<bal<=12):
#         print('High')
# else:
#     print('zehmet olmasa 1 ile 12 arasinda reqem girin')

#home work 10
# a=int(input("a: daxil edin"))

# if(0<a):
#     a=a-1
#     print(a)
# else:
#     print("musbet eded daxil edin")

#home work 11

# a=int(input('reqem daxil edin'))
# if(a>0):
#     a=a*-1
#     print(a)
# elif(a<0):
#     a=a*-1  
#     print(a)

#home work 13

name=input('adinizi daxil edin')

if(3<=len(name)<=11):
    surename=input('soyadinizi daxil edin')
    if(5<=len(surename)<=15):
        birthOfYear=input('doguldugunuz ili daxil edin')
        if(len(birthOfYear)<=4):
            mail=input('mailinizi daxil edin')
            if(10<len(mail)<22 and ('@gmail.com' in mail)):
                password1=input('parolunuzu daxil edin')
                if(6<len(password1)<13):
                    password2=input('parolunuzu tesdiqleyin')
                    if(password1==password2):
                        print('qeydiyyat tamamlandi')
                        detallar=input('qeydiyat detallarina baxmaq isteyirsiniz (he ve yaxud yox qeyd edin)')
                        if(detallar=='he'):
                            print(f'AD:{name} Soyad:{surename} Yas:{birthOfYear} Email:{mail} parol:{password1}')
                        elif(detallar=='yox'):
                            print(f'{name} {surename} ,Ugurlar')





