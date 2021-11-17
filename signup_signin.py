from modul import*
print("Регистрация и авторизация")
users=["Kristina"]
pswords=["qwerty"]
while True:
    sign=input("Регистрация- R, Авторизация- A, Закончить- E")
    if sign.upper()=="R":
        log=input("Login: ")
        pswrd1=input("Хотитите ли вы использовать автоматичсеки созданный пароль? Y- да, N- нет")
        if pswrd1.upper()=="Y":
            psword=autopsword()
            print(psword)
            pswords.append(psword) #добавляем к списку 
            if log not in users:
                users.append(log)

        elif pswrd1.upper()=="N":
            psword=""
            while len(psword)!=12:
               try:
                   psword=input("Siseta parool 12 sümboolid suurus: ")
               except:
                    ValueError
            ans=psword_check(psword) #подходит ли пароль
            if ans!= "True":
                print ("Пароль не подходит")
            else:
                users+log
                pswords+psword

    elif sign.upper()=="A":
        login=input("Siseta login: ")
        if login not in users:
            print("несуществующий пользаватель")
        else:
            psword=input("Siseta parool: ")
            if psword not in pswords:
                print("Неправильный пароль")
            else:
                print("Успешнная авторизация")
    elif sign.upper()=="E":
        break
    else:
        print("такой функции нету")