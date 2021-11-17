from random import*
def psword_check(psword:str)->str:
    """функция вернет True если пароль будет соответствовать всем параметрам
    """
    for i in range(0,13,1): #так с каждой проверкой(заглавная буква, цифра и тд)
        if psword[i].isdigit()== True:
            digit="True"
        if psword[i].isalpha()== True:
            alpha="True"
        if psword[i].isupper()== True:
            upper="True"
        if psword[i].islower()==True:
            lower="True"
        if psword[i] in [".",",","_"]:
            symbl="True"
    if digit=="True" and upper=="True" and alpha=="True" and lower=="True" and symbl=="True": #и тд со всеми вариантами
        ans="True"
    else:
        ans="False"
    return ans
def autopsword()->str:
    """auto created password
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3 #сплошной текст со всеми str
    # print(str4)
    ls = list(str4) #создает список значений каждый символ через запятую
    # print(ls)
    shuffle(ls) #перемешиваем значения
    # print(ls)
    psword = "".join([choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    # Пароль готов
    # print(psword)
    return psword