def cıkarma(x,y):
    return x-y

def toplama(x,y):
    return x+y

def bolme(x,y):
    if y == 0:
        return 'error'
    return x / y

def carpma(x,y):
    return x*y

def power(x,y):
    return x**y

def desicion(a=0):
    if not a:
        x=int(input('sayı giriniz: '))
    y=int(input('sayı giriniz: '))
    hesap=input('yapmak istediğiniz işlem 1 ise : ')
    if not a:
        return x,y,hesap
    else:
        return y,hesap

def control(x,y,hesap,func_list,eski_sonuc):
    if int(hesap) <= 5 and int(hesap) >= 1:
        print(func_list[int(hesap) - 1](x,y))
        eski_sonuc.append(func_list[int(hesap) - 1](x,y))
        if eski_sonuc[-1] == 'error':
            return 0
        a=input('yaptiginiz isleme devam etmek ister misiniz(y) :')
        if a.lower() =='y':
            return 1
        return 0
    return 0

def main():
    flag = True
    func_list = [cıkarma, toplama, bolme, carpma,power]
    eski_sonuc=[]

    a = 0
    while flag:
        if a:
            y,hesap = desicion(a)
        else:
            x,y,hesap = desicion(a)

        a = control(x,y,hesap,func_list,eski_sonuc)
        x = eski_sonuc[-1]
        if hesap == 'q':
            flag = False

if __name__ =='__main__':
    main()