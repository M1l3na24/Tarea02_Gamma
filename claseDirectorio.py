# Programa: claseDirectorio.py
# Objetivo: Programa que define la clase Directorio
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 08-09-2024

import numpy as np
import copy
import clasePersona as cP
import claseAlumno as cA
import claseProfesor as cPr
import claseCoordinador as cC


class Directorio:
    def __init__(self):
        """
        Constructor que permite crear el objeto Directorio (escolar) que sera
        un arreglo que contendra arreglos(informacion de contacto).
        Se construye como un directorio nuevo: vacio por default
        :param almacenamiento: indica el almacenamiento del directorio (0,n)
        """
        # Crear un directorio vacio
        self.directorio = np.empty(1, dtype=object)
        self.numeros_cuenta = set()
        self.numeros_profesor = set()
        self.numeros_empleado = set()
        self.num_personas = 0 # es un indice que me permite saber cual es el tamaño de mi directorio actual

    # Insertar datos de un nuevo contacto (alumno, profesor o coordinador).
    def insertar_nuevo_alumno(self):
        """
        Metodo para agregar un alumno en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de cuenta no debe de estar ya en el
        arreglo de numeros de cuenta de alumnos.
        """
        while True:
            try:
                num_cuenta = int(input('Escribe el numero de cuenta de alumno: '))
                if num_cuenta not in self.numeros_cuenta:
                    self.numeros_cuenta.add(num_cuenta)
                    break
                else:
                    print(f"El numero de cuenta {num_cuenta} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de cuenta del alumno, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del alumno: ')
        # la fecha de cumpleanios debe ser dia/mes
        cumpleanios = input('Escribe la fecha de cumpleanios del alumno: ')
        correo = input('Escribe el correo del alumno: ')
        carrera = input('Escribe la carrera del alumno: ')
        materias = list(input('Escribe las materias del alumno separadas por comas: '))

        while True:
            try:
                celular = int(input('Escribe el celular del alumno: '))
                break
            except ValueError:
                print('El celular del alumno tiene que ser un entero')
        while True:
            try:
                semestre = int(input('Escribe el semestre del alumno: '))
                break
            except ValueError:
                print('El semestre del alumno, tiene que ser un entero')
        self.directorio[self.num_personas] = cA.Alumno(nombre, celular, cumpleanios, correo, num_cuenta, carrera,
                                                       materias, semestre)
        self.num_personas += 1
        print('Alumno agregado\n')

    def insertar_nuevo_profesor(self):
        """
        Metodo para agregar un profesor en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de profesor no debe de estar ya en el
        arreglo de numero de profesores.
        """
        while True:
            try:
                num_profesor = int(input('Escribe el numero de Profesor: '))
                if num_profesor not in self.numeros_profesor:
                    self.numeros_cuenta.add(num_profesor)
                    break
                else:
                    print(f"El numero de profesor {num_profesor} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de profesor, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del profesor: ')
        # la fecha de cumpleanios debe ser dia/mes
        cumpleanios = input('Escribe la fecha de cumpleanios del profesor: ')
        correo = input('Escribe el correo del profesor: ')
        dept = input('Escribe el departamento de adscripcion del profesor: ')
        carrera = input('Escribe la carrera en la que imparte materias el profesor: ')

        grupos = list(input('Escribe los grupos del profesor separados por comas: '))

        while True:
            try:
                celular = int(input('Escribe el celular del profesor: '))
                break
            except ValueError:
                print('El celular del profesor tiene que ser un entero')
        while True:
            try:
                tel_oficina = int(input('Escribe el telefono de oficina del profesor: '))
                break
            except ValueError:
                print('El telefono de oficina del profesor, tiene que ser un entero')
        while True:
            try:
                sueldo = int(input('Escribe el sueldo del profesor: '))
                break
            except ValueError:
                print('El sueldo del profesor, tiene que ser un entero')
        self.directorio[self.num_personas] = cPr.Profesor(nombre, celular, cumpleanios, correo, num_profesor,
                                                          tel_oficina, sueldo, dept, carrera, grupos)
        self.num_personas += 1
        print('Profesor agregado\n')

    def insertar_nuevo_coordinador(self):
        """
        Metodo para agregar un Coordinador en el arreglo de directorio, para ello
        se pedira cada uno de los campos. El numero de empleado no debe de estar ya en el
        arreglo de numero de empleados.
        """
        while True:
            try:
                num_empleado = int(input('Escribe el numero de Empleado: '))
                if num_empleado not in self.numeros_empleado:
                    self.numeros_cuenta.add(num_empleado)
                    break
                else:
                    print(f"El numero de empleado {num_empleado} ya existe, escribe otro")
                    continue
            except ValueError:
                print('El numero de empleado, tiene que ser un entero')
        nombre = input('Escribe el nombre completo del Coordinador: ')
        # la fecha de cumpleanios debe ser dia/mes
        cumpleanios = input('Escribe la fecha de cumpleanios del Coordinador: ')
        correo = input('Escribe el correo del Coordinador: ')
        dept = input('Escribe el departamento de adscripcion del Coordinador: ')
        carrera_coor = input('Escribe la carrera que coordina: ')
        while True:
            try:
                celular = int(input('Escribe el celular del Coordinador: '))
                break
            except ValueError:
                print('El celular del Coordinador tiene que ser un entero')
        while True:
            try:
                tel_oficina = int(input('Escribe el telefono de oficina del Coordinador: '))
                break
            except ValueError:
                print('El telefono de oficina del Coordinador, tiene que ser un entero')
        while True:
            try:
                sueldo = int(input('Escribe el sueldo del Coordinador: '))
                break
            except ValueError:
                print('El sueldo del Coordinador, tiene que ser un entero')
        self.directorio[self.num_personas] = cC.Coordinador(nombre, celular, cumpleanios, correo, num_empleado,
                                                            tel_oficina, sueldo, dept, carrera_coor)
        self.num_personas += 1
        print('Coordinador agregado\n')

    # Mostrar la información completa de un contacto, con solo proporcionar su nombre (independientemente que sea un
    # alumno, profesor o coordinador).
    def buscar_indice(self, nombre_completo) -> int:
        """
        Metodo auxiliar que busca el indice del arreglo de directorio, dado el nombre completo de una persona
        :param nombre_completo: El nombre_completo a buscar en el directorio
        :return: indice: Int - Si se encuentra en el arreglo el directorio regresa un valor >= 0
                        Si no se encuentra en el arreglo regresa un valor < 0
        :rtype: Int
        """
        for persona in self.directorio:
            if persona is not None and persona.nombre_completo == nombre_completo:
                return int(np.where(self.directorio == persona)[0][0])
        return -1

    def esta_vacio(self) -> bool:
        """
        Metodo que verifica si esta vacio el arreglo (directorio)
        :return: True - Si esta vacio el arreglo de personas
                 False - Si hay algun elemento en el arreglo de personas
        """
        return not self.directorio.any()

    def mostrar_persona(self, nombre):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param nombre: persona a mostrar
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        if not self.esta_vacio():
            posicion = self.buscar_indice(nombre)
            persona = self.directorio[posicion]
            if isinstance(persona, cA.Alumno):
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Cuenta:\n" + str(persona.num_cuenta) + "\nCarrera:\n" + persona.carrera +
                        "\nMaterias:\n" + str(persona.materias) + "\nSemestre:\n" + str(persona.semestre))
            elif isinstance(persona, cPr.Profesor):
                cPr.setlocale(cPr.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Profesor:\n" + str(persona.num_profesor) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cPr.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera donde imparte materias:\n" +
                        persona.carrera + "\nGrupos:\n" + str(persona.grupos))

            elif isinstance(persona, cC.Coordinador):
                cC.setlocale(cC.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Empleado:\n" + str(persona.num_empleado) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cC.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera que coordina:\n" + persona.carrera_coordina)
        return "No hay contactos."

    # extra: lectura/escritura de archivos CSV
    def lectura_csvs(self):
        """
        Metodo que carga/abre la informacion de un archivo en nuestro arreglo de directorio,
        dependiendo del tipo de persona, se utilizara el constructor correspodiente.
        """
        while True:
            nombre = input('Escribe el nombre del archivo con terminación csv'
                           ', que deseas abrir: ')
            try:
                f = open(nombre, 'r')
                lineas = f.readlines()
                for linea in lineas:
                    linea = linea.split(",")
                    if linea[0] == 'A':
                        self.directorio[self.num_personas] = cA.Alumno(linea[1], int(linea[2]), linea[3], linea[4],
                                                                       int(linea[5]), linea[6], list(linea[7]),
                                                                       int(linea[8]))
                        self.numeros_cuenta.add(int(linea[5]))
                        self.num_personas += 1
                    elif linea[0] == 'P':
                        self.directorio[self.num_personas] = cPr.Profesor(linea[1], int(linea[2]), linea[3], linea[4],
                                                                          int(linea[5]), int(linea[6]), int(linea[7]),
                                                                          linea[8], linea[9], list(linea[10]))
                        self.numeros_cuenta.add(int(linea[5]))
                        self.num_personas += 1
                    elif linea[0] == 'C':
                        self.directorio[self.num_personas] = cC.Coordinador(linea[1], int(linea[2]), linea[3], linea[4],
                                                                            int(linea[5]), int(linea[6]), int(linea[7]),
                                                                            linea[8], linea[9])
                        self.numeros_cuenta.add(int(linea[5]))
                        self.num_personas += 1
                print("Archivo cargado correctamente")
                f.close()
                break
            except FileNotFoundError:
                print(f"El archivo {nombre} no existe")

    def escritura_csvs(self):
        """
        Metodo que guarda la información del arreglo de directorio, en un archivo csv
        para ello se utilizara los iteradores de cada tipo de persona
        """
        nombre = input('Escribe el nombre del archivo con terminación csv'
                       ', con el que deseas guardar: ')
        f = open(nombre, 'w')
        for persona in self.directorio:
            if persona is not None:
                per = ''
                for atributo in persona:
                    per += str(atributo) + ','
                per = per[:-1] + '\n'
                f.write(per)
        f.close()


#Mayela
    # En esta clase el metodo de ordenamiento que utilizamos fue Quick Sort
    def __particion(self, inicio, fin, comparador) -> int:
        """
        Esta función organiza los elementos del arreglo de manera que todos los elementos
        menores o iguales al pivote estén a la izquierda y todos los elementos mayores estén
        a la derecha. El pivote se coloca en su posición correcta.
        :param arreglo: int[] Arreglo de enteros
        :param inicio: La posición inicial
        :param fin: La posición final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: La posición correcta del pivote
        :rtype: int
        """
        pivote = self.directorio[inicio]
        left = inicio + 1
        right = fin
        while True:
            while left <= right and comparador(self.directorio[left], pivote) <= 0:
                left += 1
            while comparador(self.directorio[right], pivote) > 0 and right >= left:
                right -= 1
            if right < left:
                break
            else:  # Intercambiamos los datos que no cumplieron las condiciones
                self.directorio[left], self.directorio[right] = self.directorio[right], self.directorio[left]
        # Movemos el pivote a la posición correcta
        self.directorio[inicio], self.directorio[right] = self.directorio[right], self.directorio[inicio]
        return right  # Devolvemos la posición correcta del pivote

    def ordenar_directorio(self, inicio, fin, comparador): #quick sort
        """
        Esta función aplica recursivamente el algoritmo Quick Sort a los subarreglos definidos por el pivote.
        :param arreglo: int[] Arreglo de enteros
        :param inicio: La posición inicial
        :param fin: La posición final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: int[] Arreglo de enteros ordenado
        :rtype: int[]
        """
        if inicio < fin:
            posicion_part = self.__particion(self.directorio, inicio, fin, comparador)
            self.quick_sort(self.directorio, inicio, posicion_part - 1, comparador)
            self.quick_sort(self.directorio, posicion_part + 1, fin, comparador)
        return self.directorio

    def ascendente(a: cP.Persona, b: cP.Persona) -> int:
        """
        Método para determinar la relación de los Empleados con respecto a la edad
        :param a: El primer Empleado a comparar por edad
        :param b: El segundo Empleado a comparar por edad
        :return: Valor positivo si la edad de a es menor que b, cero si son iguales,
                 negativo en otro caso
        """
        return a.edad() - b.edad()

    def descendente(a: e.Empleado, b: e.Empleado) -> float:
        """
        Método para determinar la relación de los Empleados con respecto al salario
        :param a: El primer Empleado a comparar por salario
        :param b: El segundo Empleado a comparar por salario
        :return: Valor positivo si el salario de b es mayor que a, cero si son iguales,
                 negativo en otro caso
        """
        return b.salario - a.salario
    def mostrar_informacion_contacto(self, nombre, rol):
        """
        Muestra la información completa de un contacto, dado su nombre y rol.
        Los contactos se muestran ordenados.
        """
        self.ordenar_directorio()
        for persona in self.directorio:
            if isinstance(persona, rol) and persona.nombre_completo == nombre:
                print(persona)
                return
        print(f"No se encontró {rol.__name__} con el nombre: {nombre}")

    def eliminar_contacto(self, nombre):
        """
        Elimina los datos de un contacto a partir del nombre.
        """
        pass

    def actualizar_contacto(self, nombre, nuevos_datos):
        """
        Actualiza la información de un contacto a partir del nombre.
        """
        pass

    def mostrar_contactos_por_sueldo(self, sueldo):
        """
        Muestra todos los contactos con un sueldo determinado.
        La información se muestra agrupada por categoría (profesor o coordinador).
        Los contactos se muestran ordenados.
        """
        pass
















# Issac
    def contiene(self, contacto) -> bool:
        """
        Metodo que permite determinar si un contacto esta contenido en el Directorio
        :param contacto: El contacto a buscar
        :return: True si está contenido, False en caso contrario
        """
        for i in range(self.num_personas):
            if self.directorio[i] == contacto:  # Lo encontro
                return True
        return False  # No lo encontro
    def eliminar(self, contacto):
        """
        Este metodo permitira eliminar un contacto del directorio.
        :param contacto: El contacto que se va a eliminar
        """
        # Hay que asegurarnos que el arreglo no este vacío y el elemento exista
        if not self.esta_vacio() and self.contiene(contacto):
            encontro = False
            for i in range(self.num_personas):
                if self.directorio[i] == contacto:  # Lo encontro
                    if i == self.num_personas - 1:  # El elemento está al final
                        self.num_personas -= 1  # Dejamos innaccesible el elemento
                    else:  # El elemento no esta al final
                        self.num_personas -= 1
                        self.directorio[i] = self.directorio[self.directorio]
                    print(f"El contacto {contacto} fue eliminado!\n")
                    encontro = True
                    break  # Ya no es necesario seguir buscando
            if not encontro:
                print(f"El elemento {contacto} no esta en el Directorio!\n")

    def eliminar_cel(self, celular):
        """
        Elimina los datos de un contacto a partir del numero de celular.
        """
        self.ordenar_directorio() #######DEFINIR METODO ORDENAR DIRECTORIO
        for persona in self.directorio:
            if persona and persona.celular == celular:
                self.directorio.eliminar(persona)   ###### Remove no podemos usarlo
                self.num_personas -= 1
                print(f"El contacto con el numero de celular: '{celular}' ha sido eliminado.")
                return
        print(f"No se encontro contacto con el numero de celular: {celular}")

    def eliminar_email(self, correo):
        """
        Elimina los datos de un contacto a partir del correo electronico.
        """
        self.ordenar_directorio() #######DEFINIR METODO ORDENAR DIRECTORIO
        for persona in self.directorio:
            if persona and persona.email == correo:
                self.directorio.eliminar(persona)
                self.num_personas -= 1
                print(f"El contacto con el correo electrónico: '{correo}' ha sido eliminado.")
                return

    def buscar_indice_cum(self, cumpleaños) -> int:
        """
        Método auxiliar que busca el índice del arreglo de directorio, dado la fecha de cumpleaños de una persona.

        :param cumpleaños: La fecha de cumpleaños a buscar en el directorio.
        :return: El índice (int) del arreglo del directorio si se encuentra un valor >= 0.
                 Si no se encuentra en el arreglo, retorna un valor < 0.
        :rtype: int
        """
        for persona in self.directorio:
            if persona is not None and persona.fecha_cumpleanios == cumpleaños:
                return int(np.where(self.directorio == persona)[0][0])
        return -1
    def buscar_indice_cel(self, celular) -> int:
        """
        Método auxiliar que busca el índice del arreglo de directorio, dado el número de celular de una persona.

        :param celular: El número de celular a buscar en el directorio.
        :return: El índice (int) del arreglo del directorio si se encuentra un valor >= 0.
                 Si no se encuentra en el arreglo, retorna un valor < 0.
        :rtype: int
        """
        for persona in self.directorio:
            if persona is not None and persona.celular == celular:
                return int(np.where(self.directorio == persona)[0][0])
        return -1
    def buscar_contacto_celular(self, celular):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param celular: número de celular del contacro
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        if not self.esta_vacio():
            posicion = self.buscar_indice_cel(celular)
            persona = self.directorio[posicion]
            if isinstance(persona, cA.Alumno):
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Cuenta:\n" + str(persona.num_cuenta) + "\nCarrera:\n" + persona.carrera +
                        "\nMaterias:\n" + str(persona.materias) + "\nSemestre:\n" + str(persona.semestre))
            elif isinstance(persona, cPr.Profesor):
                cPr.setlocale(cPr.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Profesor:\n" + str(persona.num_profesor) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cPr.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera donde imparte materias:\n" +
                        persona.carrera + "\nGrupos:\n" + str(persona.grupos))

            elif isinstance(persona, cC.Coordinador):
                cC.setlocale(cC.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Empleado:\n" + str(persona.num_empleado) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cC.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera que coordina:\n" + persona.carrera_coordina)
        return "No hay contactos."

    def buscar_contacto_cum(self, cumpleanos):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param cumpleaños: cumpleaños del contacto
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        if not self.esta_vacio():
            posicion = self.buscar_indice_cum(cumpleanos)
            persona = self.directorio[posicion]
            if isinstance(persona, cA.Alumno):
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Cuenta:\n" + str(persona.num_cuenta) + "\nCarrera:\n" + persona.carrera +
                        "\nMaterias:\n" + str(persona.materias) + "\nSemestre:\n" + str(persona.semestre))
            elif isinstance(persona, cPr.Profesor):
                cPr.setlocale(cPr.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Profesor:\n" + str(persona.num_profesor) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cPr.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera donde imparte materias:\n" +
                        persona.carrera + "\nGrupos:\n" + str(persona.grupos))

            elif isinstance(persona, cC.Coordinador):
                cC.setlocale(cC.LC_MONETARY, "en_US")
                return ("\nNombre:\n" + persona.nombre_completo + "\nCelular:\n" + str(persona.celular) +
                        "\nCumpleanios:\n" + persona.fecha_cumpleanios + "\nCorreo:\n" + persona.email +
                        "\nNum. Empleado:\n" + str(persona.num_empleado) + "\nTel. Oficina:\n" +
                        str(persona.tel_oficina) + "\nSueldo:\n" + cC.currency(persona.sueldo, grouping=True) +
                        "\nDept. Ads.:\n" + persona.dept_ads + "\nCarrera que coordina:\n" + persona.carrera_coordina)
        return "No hay contactos."


# Carlos
    def __str__(self) -> (str,str,str):
        """
        Metodo que permitira mostrar un contacto de la clase Directorio.
        :return: Una cadena de caracteres que incluiran la informacion de contacto.
        """
        cadena = ''
        self.ordenar_directorio() #####definir ordenamiento de directorio
        alumnos = []
        profesores = []
        coordinadores = []
        for i in range(self.num_personas):
            if isinstance(self.directorio[i], cA.Alumno):
                alumnos.append(self.directorio[i])
            elif isinstance(self.directorio[i], cPr.Profesor):
                profesores.append(self.directorio[i])
            elif isinstance(self.directorio[i], cC.Coordinador):
                coordinadores.append(self.directorio[i])
        if alumnos:
            cadena + '\nAlumnos: '
            for alumno in alumnos:
                cadena + f'\n{str(alumno)}'
        else:
            cadena + '\n\nNo hay alumnos registrados'


        if profesores:
            cadena + '\n\nProfesores: '
            for profesor in profesores:
                cadena + f'\n{str(profesor)}'
        else:
            cadena + '\n\nNo hay profesores registrados'

        if coordinadores:
            cadena + '\n\nCoordinadores: '
            for coordinador in coordinadores:
                cadena + f'\n{str(coordinador)}'
        else:
            cadena + '\n\nNo hay coordinadores registrados'
        return cadena

    def mostrar_contactos_con_email(self): ###### Los datos deben mostrarse ordenados
        """
        Muestra los contactos por categoria y ordenados
        Obs: por como fue definido la clase Persona, los objetos persona
        tienen un email valido.
        """
        self.ordenar_directorio()
        copia = copy.deepcopy(self)
        copia.eliminar_email(None)
        copia.eliminar_email('')
        print(copia)

    def mostrar_contactos_de_carrera(self, carrera_particular): ###### Los datos deben mostrarse ordenados
        """
        Muestra los contactos de una carrera particular
        :param carrera_particular: str -  Nombre de la carrera
        """
        alumnos_en_carrera = []
        profesores_de_carrera = []
        coordinadores_de_carrera = []

        self.ordenar_directorio()
        for i in range(self.num_personas):
            if isinstance(self.directorio[i], cA.Alumno):
                if self.directorio[i].carrera() == carrera_particular:
                    alumnos_en_carrera.append(self.directorio[i])
            elif isinstance(self.directorio[i],cPr.Profesor):
                if self.directorio[i].carrera() == carrera_particular:
                    profesores_de_carrera.append(self.directorio[i])
            elif isinstance(self.directorio[i], cC.Coordinador):
                if self.directorio[i].carrera_coordina() == carrera_particular:
                    coordinadores_de_carrera.append(self.directorio[i])

        if alumnos_en_carrera:
            print(f'Alumnos en {carrera_particular}:')
            for alumno in alumnos_en_carrera:
                    print(alumno)
        else:
            print(f'No hay alumnos en {carrera_particular}')

        if profesores_de_carrera:
            print(f'Profesores de {carrera_particular}:')
            for profesor in profesores_de_carrera:
                print(profesor)
        else:
            print(f'No hay profesores de {carrera_particular}')

        if coordinadores_de_carrera:
            print(f'Coordinadores de {carrera_particular}:')
            for coordinador in coordinadores_de_carrera:
                    print(coordinador)
        else:
            print(f'No hay coordinadores de {carrera_particular}')

    def mostrar_alumnos_o_profesores(self, eleccion):
        """
        Muestra solo los alumnos o solo los maestros en orden
        Esto segun la eleccion del usuario
        :param eleccion: 0 si alumnos, 1 si maestros
        """

        self.ordenar_directorio()
        if eleccion == 0:
            alumnos = []
            for i in range(self.num_personas):
                if isinstance(self.directorio[i], cA.Alumno):
                    alumnos.append(self.directorio[i])
            if alumnos:
                print('\nAlumnos registrados:')
                for alumno in alumnos:
                    print(alumno)
            else:
                print('\nNo hay alumnos registrados')

        elif eleccion == 1:
            profesores = []
            for persona in self.directorio:
                if isinstance(persona, cPr.Profesor):
                    profesores.append(persona)
            if profesores:
                print('\nProfesores registrados:')
                for profesor in profesores:
                    print(profesor)
            else:
                print('\nNp hay profesores registrados')
        else:
            print('No es una entrada valida')
