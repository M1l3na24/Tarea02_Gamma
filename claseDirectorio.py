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
        """
        # Crear un directorio vacio
        self.directorio = np.empty(1, dtype=object)
        self.numeros_cuenta = set()
        self.numeros_profesor = set()
        self.numeros_empleado = set()
        # num_personas es un indice que me permite saber cual es el tamaño de mi directorio actual
        self.num_personas = 0

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
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del alumno (dia/mes/anio): ')
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
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del profesor (dia/mes/anio): ')
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
        # la fecha de cumpleanios debe ser dia/mes/anio
        cumpleanios = input('Escribe la fecha de cumpleanios del Coordinador (dia/mes/anio): ')
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

    # Extra: lectura/escritura de archivos CSV
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

    # En esta clase el metodo de ordenamiento que utilizamos fue Quick Sort

    def __particion(self, inicio, fin, comparador) -> int:
        """
        Esta funcion organiza los elementos del directorio de manera que todos los elementos
        menores o iguales al pivote estan a la izquierda y todos los elementos mayores estan
        a la derecha. El pivote se coloca en su posicion correcta.
        :param inicio: La posición inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: La posicion correcta del pivote
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

    # Quick sort
    def ordenar_directorio(self, inicio, fin, comparador):
        """
        Esta funcion aplica recursivamente el algoritmo Quick Sort a los subarreglos definidos por el pivote.
        :param inicio: La posicion inicial
        :param fin: La posicion final
        :param comparador: El comparador con el que se desea hacer el ordenamiento
        :return: Arreglo de contactos ordenado
        """
        if inicio < fin:
            posicion_part = self.__particion(inicio, fin, comparador)
            self.ordenar_directorio(inicio, posicion_part - 1, comparador)
            self.ordenar_directorio(posicion_part + 1, fin, comparador)
        return self.directorio

# Tipos de comparadores: Ordenar alfabeticamente
    def __compare_strings(self, str1: str, str2: str) -> int:
        """
        Metodo privado para comparar dos cadenas y devolver su relacion de orden en terminos de un int
        :param str1: Primera cadena a comparar
        :param str2: Segunda cadena a comparar
        :return: -1 si str1 lexicograficamente es menor que str2, 0 si son iguales, 1 en otro caso
        """
        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0

    def nombre_comparador(self, a: cP.Persona.nombre_completo, b: cP.Persona.nombre_completo):
        """
        Metodo para determinar la relacion de los Contactos con respecto al nombre.
        :param a: El nombre del primer Contacto a comparar
        :param b: El nombre del segundo Contacto a comparar
        :return: Valor positivo si el nombre de a es mayor que b, negativo si el nombre de
                 b es mayo que a. Si es el mismo nombre, regresa un 0.
        """
        dif_nombre = self.__compare_strings(a, b)
        return dif_nombre

    def mostrar_informacion_contacto(self, nombre, rol):
        """
        Muestra la informacion completa de un contacto, dado su nombre y rol.
        La informacion se muestra agrupada por categoria (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param nombre:str -el nombre completo del contacto
        :param rol - tipo de objeto
        :return un string con la informacion completa del contacto con esas caracteristicas.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        for contacto in self.directorio:
            if contacto.nombre_completo == nombre and isinstance(contacto, rol):
                return contacto
        print('No existe un contacto con esas caracteristicas')

    def eliminar_contacto(self, nombre):
        """
        Elimina los datos de un contacto a partir del nombre.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        for persona in self.directorio:
            if persona and persona.nomnre_completo == nombre:
                self.eliminar(persona)
                print(f"El contacto con el nombre: '{nombre}' ha sido eliminado.")
            else:
                print(f"No se encontro contacto con el nombre completo: {nombre}")

    def menu_actualizar_alumno(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Alumno
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Cuenta\n'
                           '6. Carrera \n'
                           '7. Materias\n'
                           '8. Semestre\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def menu_actualizar_profesor(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Profesor
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Profesor\n'
                           '6. Tel. Oficina \n'
                           '7. Sueldo\n'
                           '8. Dept. Adscripcion\n'
                           '9. Carrera donde imparte materias\n'
                           '10. Grupos\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,9,10,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def menu_actualizar_coordinador(self) -> str:
        """
        Metodo auxiliar, que muestra en pantalla las opciones para actualizar un Profesor
        :return: opcion: Int - La opcion deseada para actualizar
        :rtype: Str
        """
        while True:
            opcion = input('Que deseas actualizar:\n'
                           '1. Nombre Completo\n'
                           '2. Celular\n'
                           '3. Fecha Cumpleanios\n'
                           '4. Email\n'
                           '5. Num. Empleado\n'
                           '6. Tel. Oficina \n'
                           '7. Sueldo\n'
                           '8. Dept. Adscripcion\n'
                           '9. Carrera que coordina\n'
                           'S. Salir \n').upper()
            if opcion not in '1,2,3,4,5,6,7,8,9,S' or len(opcion) != 1:
                print("Opcion invalida.")
                continue
            else:
                break
        return opcion

    def actualizar_alumno(self):
        """
        Metodo para actualizar un contacto del tipo allumno, si se encuentra el nombre completo del alumno
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nom_completo = input('Escribe el nombre completo del alumno: ')
        indice = self.buscar_indice(nom_completo)
        if indice == -1:
            print(f"No se encuentra el alumno con nombre completo {nom_completo}")
        else:
            alumno = self.directorio[indice]
            if isinstance(alumno, cA.Alumno) and not isinstance(alumno, cPr.Profesor):
                print(alumno)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_alumno()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del Alumno a actualizar: ')
                            alumno.nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del alumno: '))
                            alumno.celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del alumno: '))
                            alumno.fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del alumno: ')
                            alumno.email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumcuenta = int(input('Escribe el nuevo numero de cuenta del alumno: '))
                                    break
                                except ValueError:
                                    print('El numero de cuenta del alumno, tiene que ser un entero')
                            self.numeros_cuenta.remove(alumno.num_cuenta)
                            alumno.num_cuenta = nuevonumcuenta
                            self.numeros_cuenta.add(alumno.num_cuenta)
                            print('Numero de Cuenta Actualizado \n')
                            opcion = ''

                        case "6":
                            nueva_carrera = input('Escribe la nueva carrera del alumno: ')
                            alumno.carrera = nueva_carrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case "7":
                            nuevamaterias = list(input('Escribe la nueva lista de materias del alumno: '))
                            alumno.materias = nuevamaterias
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "8":
                            nuevsemestre = int(input('Escribe la nueva lista de materias del alumno: '))
                            alumno.semestre = nuevsemestre
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el alumno con nombre {nom_completo}")

    def actualizar_profesor(self):
        """
        Metodo para actualizar un contacto del tipo Profesor, si se encuentra el nombre completo del profesor
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nomcompleto = input('Escribe el nombre completo del profesor: ')
        indice = self.buscar_indice(nomcompleto)
        if indice == -1:
            print(f"No se encuentra el profesor con nombre completo {nomcompleto}")
        else:
            profesor = self.directorio[indice]
            if isinstance(profesor, cPr.Profesor) and not isinstance(profesor, cC.Coordinador):
                print(profesor)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_profesor()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del profesor a actualizar: ')
                            profesor.nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del profesor: '))
                            profesor.celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del profesor: '))
                            profesor.fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del profesor: ')
                            profesor.email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumprofesor = int(input('Escribe el nuevo numero de profesor: '))
                                    break
                                except ValueError:
                                    print('El numero de cuenta del profesor, tiene que ser un entero')
                            self.numeros_profesor.remove(profesor.num_cuenta)
                            profesor.num_cuenta = nuevonumprofesor
                            self.numeros_profesor.add(profesor.num_cuenta)
                            print('Numero de Profesor Actualizado \n')
                            opcion = ''

                        case "6":
                            nuevoteloficina = int(input('Escribe el nuevo telefono de oficina del profesor: '))
                            profesor.tel_oficina = nuevoteloficina
                            print('Tel. Oficina Actualizado \n')
                            opcion = ''

                        case "7":
                            nuevosueldo = int(input('Escribe el nuevo sueldo del profesor: '))
                            profesor.sueldo = nuevosueldo
                            print('Sueldo Actualizado \n')
                            opcion = ''

                        case "8":
                            nuevodeptads = input('Escribe el nuevo Dept. de Ads. del profesor: ')
                            profesor.dept_ads = nuevodeptads
                            print('Dept. de Ads. Actualizado \n')
                            opcion = ''

                        case "9":
                            nuevocarrera = input('Escribe la nueva carrera donde imparte materias el profesor: ')
                            profesor.dept_ads = nuevocarrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case '10':
                            nuevgrup = list(input('Escribe la nueva lista de grupos del profesor: '))
                            profesor.grupos = nuevgrup
                            print('Materias Actualizadas \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el profesor con nombre {nomcompleto}")

    def actualizar_coordinador(self):
        """
        Metodo para actualizar un contacto del tipo Coordinador, si se encuentra el nombre completo del coordinador
        desplegara un menu para saber que valor actualizar. Si no imprimira un mensaje.
        """
        nomcompleto = input('Escribe el nombre completo del coordinador: ')
        indice = self.buscar_indice(nomcompleto)
        if indice == -1:
            print(f"No se encuentra el coordinador con nombre completo {nomcompleto}")
        else:
            coordinador = self.directorio[indice]
            if isinstance(coordinador, cC.Coordinador) and not isinstance(coordinador, cPr.Profesor):
                print(coordinador)
                opcion = ''
                while opcion != 'S':
                    opcion = self.menu_actualizar_coordinador()

                    match opcion:
                        case "1":
                            nuevonombre = input('Escribe el nuevo nombre del coordinador a actualizar: ')
                            coordinador.nombre_completo = nuevonombre
                            print('Nombre Actualizado \n')
                            opcion = ''

                        case "2":
                            nuevocelular = int(input('Escribe la nuevo celular del coordinador: '))
                            coordinador.celular = nuevocelular
                            print('Celular Actualizado \n')
                            opcion = ''

                        case "3":
                            nuevocumple = int(input('Escribe el nuevo cumpleanios del coordinador: '))
                            coordinador.fecha_cumpleanios = nuevocumple
                            print('Cumpleanios Actualizado \n')
                            opcion = ''

                        case "4":
                            nuevoemail = input('Escribe el nuevo email del coordinador: ')
                            coordinador.email = nuevoemail
                            print('Email Actualizado \n')
                            opcion = ''

                        case "5":
                            while True:
                                try:
                                    nuevonumempleado = int(
                                        input('Escribe el nuevo numero de empleado del coordinador: '))
                                    break
                                except ValueError:
                                    print('El numero de empleado del coordinador, tiene que ser un entero')
                            self.numeros_empleado.remove(coordinador.num_empleado)
                            coordinador.num_empleado = nuevonumempleado
                            self.numeros_empleado.add(coordinador.num_empleado)
                            print('Numero de Empleado Actualizado \n')
                            opcion = ''

                        case "6":
                            nuevoteloficina = int(input('Escribe el nuevo telefono de oficina del coordinador: '))
                            coordinador.tel_oficina = nuevoteloficina
                            print('Tel. Oficina Actualizado \n')
                            opcion = ''

                        case "7":
                            nuevosueldo = int(input('Escribe el nuevo sueldo del coordinador: '))
                            coordinador.sueldo = nuevosueldo
                            print('Sueldo Actualizado \n')
                            opcion = ''

                        case "8":
                            nuevodeptads = input('Escribe el nuevo Dept. de Ads. del coordinador: ')
                            coordinador.dept_ads = nuevodeptads
                            print('Dept. de Ads. Actualizado \n')
                            opcion = ''

                        case "9":
                            nuevocarrera = input('Escribe la nueva carrera que coordina: ')
                            coordinador.dept_ads = nuevocarrera
                            print('Carrera Actualizada \n')
                            opcion = ''

                        case "S":
                            print('Volviendo ...')
            else:
                print(f"No se encuentra el coordinador con nombre {nomcompleto}")

    def mostrar_contactos_por_sueldo(self, sueldo: int):
        """
        Muestra todos los contactos con un sueldo determinado.
        La información se muestra agrupada por categoría (profesor o coordinador).
        Los contactos se muestran ordenados.
        :param sueldo: int - el sueldo especifico que busco
        :return un string ordenado que divide profesores y coordinadores con ese sueldo especifico.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        profesores = ''
        coordinadores = ''
        for contacto in self.directorio:
            if contacto is not None and contacto.sueldo == sueldo:
                if isinstance(contacto, cPr.Profesor):
                    profesores += str(contacto) + '\n'
                if isinstance(contacto, cC.Coordinador):
                    coordinadores += str(contacto) + '\n'
        return "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores

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
                    if i == self.num_personas - 1:  # El elemento esta al final
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
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        for persona in self.directorio:
            if persona and persona.celular == celular:
                self.eliminar(persona)
                print(f"El contacto con el numero de celular: '{celular}' ha sido eliminado.")
                return
        print(f"No se encontro contacto con el numero de celular: {celular}")

    def eliminar_email(self, correo):
        """
        Elimina los datos de un contacto a partir del correo electronico.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        for persona in self.directorio:
            if persona and persona.email == correo:
                self.eliminar(persona)
                print(f"El contacto con el correo electrónico: '{correo}' ha sido eliminado.")
                return

    def buscar_indice_cum(self, cumpleanios) -> int:
        """
        Método auxiliar que busca el índice del arreglo de directorio, dado la fecha de cumpleaños de una persona.

        :param cumpleanios: La fecha de cumpleaños a buscar en el directorio.
        :return: El índice (int) del arreglo del directorio si se encuentra un valor >= 0.
                 Si no se encuentra en el arreglo, retorna un valor < 0.
        :rtype: int
        """
        for persona in self.directorio:
            if persona is not None and persona.fecha_cumpleanios == cumpleanios:
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

    def buscar_contacto_celular(self, celular: int):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio.
        La representa a traves de los elementos en el array.
        :param celular:int - numero de celular del contacto
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        if not self.esta_vacio():
            alumnos = ''
            profesores = ''
            coordinadores = ''
            for contacto in self.directorio:
                if contacto is not None and contacto.celular == celular:
                    if isinstance(contacto, cA.Alumno):
                        alumnos += str(contacto) + '\n'
                    if isinstance(contacto, cPr.Profesor):
                        profesores += str(contacto) + '\n'
                    if isinstance(contacto, cC.Coordinador):
                        coordinadores += str(contacto) + '\n'
                return "\nALUMNOS:\n" + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores
        return "No hay contactos."

    def buscar_contacto_cum(self, cumpleanios: int):
        """
        Metodo __str__ que define como mostrar una persona dentro del directorio a partir de su cumpleanios.
        La representa a traves de los elementos en el directorio.
        :param cumpleanios: cumpleanios del contacto
        :return: cadena: Str - La representacion de la persona en el directorio
        :rtype: Str
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        if not self.esta_vacio():
            alumnos = ''
            profesores = ''
            coordinadores = ''
            for contacto in self.directorio:
                if contacto is not None and contacto.cumpleanios == cumpleanios:
                    if isinstance(contacto, cA.Alumno):
                        alumnos += str(contacto) + '\n'
                    if isinstance(contacto, cPr.Profesor):
                        profesores += str(contacto) + '\n'
                    if isinstance(contacto, cC.Coordinador):
                        coordinadores += str(contacto) + '\n'
                return "\nALUMNOS:\n" + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores
        return "No hay contactos."

    # Carlos

    def __str__(self) -> (str, str, str):
        """
        Metodo que permitira mostrar un contacto de la clase Directorio.
        :return: Una cadena de caracteres que incluiran la informacion de contacto.
        """
        cadena = ''
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
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
            cadena += '\nAlumnos: '
            for alumno in alumnos:
                cadena += f'\n{str(alumno)}'
        else:
            cadena += '\n\nNo hay alumnos registrados'

        if profesores:
            cadena += '\n\nProfesores: '
            for profesor in profesores:
                cadena += f'\n{str(profesor)}'
        else:
            cadena += '\n\nNo hay profesores registrados'

        if coordinadores:
            cadena += '\n\nCoordinadores: '
            for coordinador in coordinadores:
                cadena += f'\n{str(coordinador)}'
        else:
            cadena += '\n\nNo hay coordinadores registrados'
        return cadena

    def mostrar_contactos_con_email(self):
        """
        Muestra los contactos por categoria y ordenados
        Obs: por como fue definido la clase Persona, los objetos persona
        tienen un email valido.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        copia = copy.deepcopy(self)
        copia.eliminar_email(None)
        copia.eliminar_email('')
        print(copia)

    def mostrar_contactos_por_carrera(self, carrera_particular: str):
        """
        Muestra todos los contactos con una carrera particular.
        La información se muestra agrupada por categoría (alumno, profesor o coordinador).
        Los contactos se muestran ordenados.
        :param carrera_particular: str -la carrera especifica que busco
        :return un string ordenado que divide alumnos, profesores y coordinadores con esa carrera especifica.
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
        alumnos = ''
        profesores = ''
        coordinadores = ''
        for contacto in self.directorio:
            if isinstance(contacto, cA.Alumno) and contacto.carrera == carrera_particular:
                alumnos += str(contacto) + '\n'
            elif isinstance(contacto, cPr.Profesor) and contacto.carrera == carrera_particular:
                profesores += str(contacto) + '\n'
            elif isinstance(contacto, cC.Coordinador) and contacto.carrera_coordina == carrera_particular:
                coordinadores += str(contacto) + '\n'

        return "\nALUMNOS:\n" + alumnos + "\nPROFESORES:\n" + profesores + "\nCOORDINADORES:\n" + coordinadores

    def mostrar_alumnos_o_profesores(self, eleccion):
        """
        Muestra solo los alumnos o solo los maestros en orden
        Esto segun la eleccion del usuario
        :param eleccion: 0 si alumnos, 1 si maestros
        """
        self.ordenar_directorio(0, self.num_personas, self.nombre_comparador)
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
