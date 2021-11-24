def file(file:str)->str:
	"""Loeme teksti failist
	"""
	f=open(file, "r")
	stroka=f.read() # read - читает файл как текст применяя все нечитаемые символы
	# stroka=f.readlines() # readlines - создает список в которой каждая новая строка отдельный элемент списка
	f.close()
	return stroka
	
textresult=file("filetxt.txt")
print(textresult)

def read_file_list(file:str)->list:
	"""Loeme tekst failist ja salvesta järjendisse
	"""
	f=open(file, "r")
	list=[]
	for stroka in f:
		list.append(stroka.strip())
	f.close()
	return list

listresult=read_file_list("filetxt.txt")
print(listresult)

def file_write(file:str):
	"""Salvesta text failisse
	"""
	f=open(file,"a")
	text=input("Siseta tekst: ")
	f.write(text+"\n")
	f.close()

#for i in range(10):
	#file_write("Loetelu.txt")

def change_text_in_fail(fail:str):
	text=input("Siseta uus tekst: ")
	with open(file, "w") as f:
		f.write(text+"\n")

change_text_in_fail(input("faili nimetus:"))
