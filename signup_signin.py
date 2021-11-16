from modul import*
print("Регистрация и авторизация")
s1=[]
s2=[]
while True:
    sign=input("Регистрация- R, Авторизация- A, Закончить- E")
    if sign.upper()=="R":
        log=input("Login: ")
        pswrd1=input("Хотитите ли вы использовать автоматичсеки созданный пароль? Y- да, N- нет")
        if pswrd1.upper=="Y":
            psword=autopsword
        elif psword1.upper=="N":
            psword=""
            while len(psword)!=12:
               try:
                   psword=input("Siseta parool: ")
               except:
                    ValueError
            ans=psword_check(a) #подходит ли пароль
        #s1+log
        #s2+psword
    elif sign.upper()=="A":
        login=input("Siseta login: ")
        psword=input("Siseta parool: ")
        if login not in s1:
            pass
        if psword not in s2:
            pass
    else:
        break