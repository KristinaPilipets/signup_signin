from modul import*
print("Регистрация и авторизация")
while True: 
    sign=input("Регистрация- R, Авторизация- A")
    if sign.upper()=="R":
        log=input("Login: ")
        pswrd1=input("Хотитите ли вы использовать автоматичсеки созданный пароль? Y- да, N- нет")
        if pswrd1.upper=="Y":
            psword=autopsword
        elif psword1.upper=="N":

    elif sign.upper()=="A":
        pass
