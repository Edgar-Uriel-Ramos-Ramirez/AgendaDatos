from io import open

import os

class Contacto(object):
	def __init__(self, nomb="", ApP="", ApM="", dire="", sex="", email="", NumTel="", NumCiud=""):
		self.nombre = nomb
		self.apellidoPaterno = ApP
		self.apellidoMaterno = ApM
		self.direccion = dire
		self.sexo = sex
		self.correo = email
		self.numeroTelefono = NumTel
		self.numeroCiudadano = NumCiud
	
	#def imprimirContactos(self):

class Agenda(object):
	def __init__(self):
		pass

	def escribirAgenda(self, ContactoNew):
		archivoAgregado = open("ArchivosCargados","a")
		
		archivoAgregado.write("Nombre: " + ContactoNew.nombre + '\n')
		archivoAgregado.write("Apellido Paterno: " + ContactoNew.apellidoPaterno + '\n')
		archivoAgregado.write("Apellido Materno: " + ContactoNew.apellidoMaterno + '\n')
		archivoAgregado.write("Direccion: " + ContactoNew.direccion + '\n')
		archivoAgregado.write("Sexo: " + ContactoNew.sexo + '\n')
		archivoAgregado.write("Correo: " + ContactoNew.correo + '\n')
		archivoAgregado.write("Numero de Telefono: " + ContactoNew.numeroTelefono + '\n')
		archivoAgregado.write("Numero Ciudadano: " + ContactoNew.numeroCiudadano + '\n')
		archivoAgregado.write("----------------------------------------------------\n")
		archivoAgregado.close()

	def LeerContactos(self):
		archivoAgregado = open("ArchivosCargados","r")  #Abrimos el archivo como modo lectura

		for linea in archivoAgregado: #Recorremos todas las lineas del archivo...
			print (linea,end="")   #... y las imprimimos

	def buscarContacto(self):
		nom = input("\nPorfavor. Escriba su Hermoso Nombre a Buscar: ")
		print("\n")
		archivoAgregado = open("ArchivosCargados","r")  #Abrimos el archivo como modo lectura
		contactoCorrecto = 0
		for linea in archivoAgregado: #Recorremos todas las lineas del archivo...
			if nom in linea:  # Edgar  IN  "Nombre: Edgar Uriel\n"
				contactoCorrecto = 8
			if contactoCorrecto:
				print(linea, end="")
				contactoCorrecto = contactoCorrecto - 1
		archivoAgregado.close()

	def elminiarContacto(self):
		nom = input("Porfavor. Escriba su Feo Nombre a Eliminar: ")
		# Crear un nuevo archivo copia
		archivoAgregado    = open("ArchivosCargados"   ,"r")
		archivoAgregadoTMP = open("ArchivosCargadosTMP","a")
		contactoIncorrecto = 0
		for linea in archivoAgregado:
			if nom in linea:
				contactoIncorrecto = 9
			if contactoIncorrecto == 0:
				archivoAgregadoTMP.write(linea)
			else:
				contactoIncorrecto = contactoIncorrecto - 1
		archivoAgregado.close()
		archivoAgregadoTMP.close()

		archivoAgregado    = open("ArchivosCargados"   ,"w")
		archivoAgregadoTMP = open("ArchivosCargadosTMP","r")
		for linea in archivoAgregadoTMP:
			archivoAgregado.write(linea)
		archivoAgregado.close()
		archivoAgregadoTMP.close()
		os.remove("ArchivosCargadosTMP")
		
	def modificarContacto(self, nombre, opcion, nuevoValor):
		# Crear un nuevo archivo copia
		archivoAgregado    = open("ArchivosCargados"   ,"r")
		archivoAgregadoTMP = open("ArchivosCargadosTMP","a")
		contactoIncorrecto = 0
		for linea in archivoAgregado:
			if nombre in linea:
				contactoIncorrecto = 9
			if contactoIncorrecto == 0:
				archivoAgregadoTMP.write(linea)
			else:
				if contactoIncorrecto == 9 and opcion == 1:
					archivoAgregadoTMP.write("Nombre: " + nuevoValor + '\n')
				elif contactoIncorrecto == 8 and opcion == 2:
					archivoAgregadoTMP.write("Apellido Paterno: " + nuevoValor + '\n')
				elif contactoIncorrecto == 7 and opcion == 3:
					archivoAgregadoTMP.write("Apellido Materno: " + nuevoValor + '\n')
				elif contactoIncorrecto == 6 and opcion == 4:
					archivoAgregadoTMP.write("Direccion: " + nuevoValor + '\n')
				elif contactoIncorrecto == 5 and opcion == 5:
					archivoAgregadoTMP.write("Sexo: " + nuevoValor + '\n')
				elif contactoIncorrecto == 4 and opcion == 6:
					archivoAgregadoTMP.write("Correo: " + nuevoValor + '\n')
				elif contactoIncorrecto == 3 and opcion == 7:
					archivoAgregadoTMP.write("Numero de Telefono: " + nuevoValor + '\n')
				elif contactoIncorrecto == 2 and opcion == 8:
					archivoAgregadoTMP.write("Numero Ciudadano: " + nuevoValor + '\n')
				elif contactoIncorrecto == 1:
					archivoAgregadoTMP.write("----------------------------------------------------\n")
				else:
					archivoAgregadoTMP.write(linea)
				contactoIncorrecto = contactoIncorrecto - 1
		archivoAgregado.close()
		archivoAgregadoTMP.close()

		archivoAgregado    = open("ArchivosCargados"   ,"w")
		archivoAgregadoTMP = open("ArchivosCargadosTMP","r")
		for linea in archivoAgregadoTMP:
			archivoAgregado.write(linea)
		archivoAgregado.close()
		archivoAgregadoTMP.close()
		os.remove("ArchivosCargadosTMP")

	def menu(self):
		while True:
			#os.system('clear') # Este va junto con el metodo que importamos que sirve para limpiar en automatico nuestra pantalla
			print("     " + "\n SEA BIENVENIDO A LA AGENDA TELEFONICA EN PYTHON :) \n" + "         ")
			print("		" +	 "  **************   MENU   *************************    " + "         ")
			print("\n")
			print("Sleccione una OPCION A EJECUTAR")
			print("1.- Registrar Contacto :) ")
			print("2.- Listar Contacto :) ")
			print("3.- Modificar Contacto :)")
			print("4.- Buscar Contacto :) ")
			print("5.- ELiminar Contacto :) ")
			print("6.- Salir :) ")

			# El try es para atrapar los errores que elija el usuario, es lo mismo como JAVA, XD
			try: 
				opcion = int(input("\nIngrese la opcion a elegir compañero: "))
			except:
				print("HOLA COMPAÑERO, USTED ACABA DE ELEJIR UNA OPCION QUE NO ESTA EN LA TABLITA")
				input() # Aqui este metodo sirve para que el Usuario vea el mensajito y vea que elijio una opcion no valida
				continue # Esta opcion si se puede llamar asi, su funcion es de que al momento de que el usuario presione Enter, lo que va hacer es entrar en el ciclo while
					
			if opcion == 1: #Aqui vamos hacer los registros respectivos
				nombre = input("Porfavor. Escriba su Hermoso Nombre: ")
				apellidoPaterno = input("Porfavor. Ingrese su Apellido Paterno: ")
				apellidoMaterno = input("Porfavor. Ingrese su Apellido Materno: ")
				direccion = input("Porfavor. Ingrese su Direccion de casa: ")
				sexo = input("Porfavor. Ingrese su Sexo " + "H/M: ")
				correo = input("Porfavor. Ingrese su Correo Electronico: ")
				numeroTelefono = input("Porfavor. Ingrese su Numero de Telefono: ")
				numeroCiudadano = input("Porfavor. Ingrese su Numero de Ciudadano: ")

				c1 = Contacto(nombre, apellidoPaterno, apellidoMaterno, direccion, sexo, correo, numeroTelefono, numeroCiudadano)
				self.escribirAgenda(c1)

			if opcion == 2: # Imprimir o listar los Contactos Agregados
				self.LeerContactos()

			if opcion == 3:
				nombreABuscar = input("Ingresa el nombre a buscar: ")
				print("\n Introduce el atributo a modificar: \n")
				print("*****************************************************\n")
				print("1 [NOMBRE] \n")
				print("2 [Apellido Paterno] \n")
				print("3 [Apellido Materno] \n")
				print("4 [Direccion] \n")
				print("5 [Sexo]\n")
				print("6 [Correo Electronico]\n")
				print("7 [Numero de Telefono] \n")
				print("8 [Numero Ciudadano]\n")
				print("****************************************************** \n")
				opcion = int(input("\nIngrese la opcion a elegir compañero: "))
				valor = input("\n Ingresa el valor nuevo del atributo compañero: ")
				self.modificarContacto(nombreABuscar, opcion, valor)

			if opcion == 4: 
				self.buscarContacto()

			if opcion == 5: 
				self.elminiarContacto()

			if opcion == 6:
				exit()


instanciaAgenda = Agenda()
instanciaAgenda.menu()
