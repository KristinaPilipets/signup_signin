from modul import*
print("Regestreerimne ja Autoriseerimine".center(50,"+"))
while True:
    sign=input("Regestreerimne- R, Autoriseerimine- A, Välja- E")
    if sign.upper()=="R":
        signup()
    elif sign.upper()=="A":
        signin()
    elif sign.upper()=="E":
        break
    else:
        print("See funktsioon ei ole")