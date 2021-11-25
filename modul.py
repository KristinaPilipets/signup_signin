from random import*

def allusers():
    """Пример функции
    """
    i=0
    for login in users:
        print(login,end="-")
        print(pswords[i])
        i+=1

def psword_check(psword:str)->bool:
    """функция вернет True если пароль будет соответствовать всем параметрам
    """
    digit="d"
    alpha="a"
    upper="e"
    lower="f"
    symbl="w"
    psword=list(psword)
    for i in psword:
        if i.isdigit()== True: #string index out of range
            digit="True"
        if i.isalpha()== True:
            alpha="True"
        if i.isupper()== True:
            upper="True"
        if i.islower()==True:
            lower="True"
        if i in [".","_","/","@"]:
            symbl="True"
    if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and symbl=="True": 
        ans=True
    else:
        ans=False
    return ans

def autopsword()->str:
    """automaatseltloomatud parool
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3 #сплошной текст со всеми str
    ls = list(str4) #создает список значений каждый символ через запятую ["q","w","1"...и тд]
    shuffle(ls) #перемешиваем значения
    psword = "".join([choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    # Пароль готов
    return psword

def signup():
    """Регистрация пользывателя, выбор метода создания пароля.
    """
    f=open('users.txt', 'r')
    users=[]
    for stroka in f:
        users.append(stroka.strip())
    f.close()
    log=input("Siseta login: ")
    while log in users:
         try:
             log=input("login: ")
         except:
                ValueError
    with open("users.txt", "a") as user:
        user.write(log+"\n")
    pswrd1=""
    while pswrd1 not in ["Y","y","N","n"]:
        try:
            pswrd1=input("Kas sa tahad kasutada automaatseltloomatud parool? Y- jah, N- ei")
        except:
            ValueError
    if pswrd1.upper()=="Y":
       pswordA=autopsword()
       print("sinu parool: "+pswordA)
       with open("pswords.txt", "a") as psword1:
            psword1.write(pswordA + "\n")
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
             with open("pswords.txt", "a") as pswrd:
                pswrd.write(psword + "\n")

def signin():
    """Регистрация проверка по чписку пароля и логина, при необходимости справшивает пользователя о регестрации и предлагагет выбор при ответе "да" перекидывем на функцию ркгистрации
    """
    f=open('users.txt', 'r')
    userslist=[]
    for stroka in f:
        userslist.append(stroka.strip())
    f.close()
    login=input("Siseta login: ")
    print(userslist)
    if login not in userslist:
        print("Kasutaja ei ole olema")
        print("Kas sa tahad regestreerida?")
        reg=""
        while reg not in ["N","n","Y","y"]:
            try:
                reg=input("Y= jah, N= ei")
            except:
                ValueError
        if reg.upper() =="Y":
            signup()
    else:
        pswords1 = open('pswords.txt', 'r')
        pswords=[]
        for string in pswords1:
            pswords.append(string.strip())
        pswords1.close()
        print(pswords)
        psword=input("Siseta parool: ")
        if psword not in pswords:
            print("Vale parool")
        else:
            if userslist.index(login) != pswords.index(psword):
                print("Autoriseerimine ei ole edukas")
            else:
                print("Autoriseerimine on edukas")