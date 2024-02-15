from io import open

# archivo1=open('archivo.txt','a')
# archivo1.write("\n Hola mundo")
# archivo1.close()

archivo1=open('archivo.txt','r')
# print(archivo1.read())
# ##Seek reinicia la lectura hasta alguna posición podiendo así leer varias veces un archivo
# archivo1.seek(0)
# print(archivo1.read())

#print(archivo1.readlines())

archivo1.close()