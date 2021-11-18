from modul import*
print("Regestreerimne ja Autoriseerimine".center(50,"+"))
users=["Kristina"]
pswords=["qwerty"]
while True:
    sign=input("Regestreerimne- R, Autoriseerimine- A, Välja- E")
    if sign.upper()=="R":
        log=input("Login: ")
        pswrd1=input("Kas sa tahad kasutada automaatseltloomatud parool? Y- jah, N- ei")
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
            if ans != True:
                print ("Parool ei sobi")
            else:
                print("Regestreerimne on edukas")
                users.append(log)
                pswords.append(psword)

    elif sign.upper()=="A":
        login=input("Siseta login: ")
        if login not in users:
            print("Kasutaja ei ole olemas")
        else:
            psword=input("Siseta parool: ")
            if psword not in pswords:
                print("Vale parool")
            else:
                print("Autoriseerimine on edukas")
    elif sign.upper()=="E":
        break
    else:
        print("See funktsioon ei ole")