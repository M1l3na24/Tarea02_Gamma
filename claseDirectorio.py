# Programa: claseDirectorio.py
# Objetivo: Programa que define la clase Directorio
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 02-09-2024

import numpy as np
# import clasePersona as cP
import claseAlumno as cA
import claseProfesor as cPr
import claseCoordinador as cC


class Directorio:
    def __init__(self, almacenamiento):
        """
        Constructor que permite crear el objeto Directorio (escolar) que sera
        un arreglo que contendra arreglos(informacion de contacto).
        Se construye como un directorio nuevo: vacio por default
        :param almacenamiento: indica el almacenamiento del directorio (0,n)
        """
        # Crear un directorio vacio
        self.directorio = np.empty(almacenamiento, dtype=object)
        self.numeros_cuenta = set()
        self.numeros_profesor = set()
        self.numeros_empleado = set()
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

    def eliminar_cel(self, celular):
        """
        Elimina los datos de un contacto a partir del número de celular.
        """
        self.ordenar_directorio()
        for persona in self.directorio:
            if persona and persona.celular == celular:
                self.directorio.remove(persona)
                self.num_personas -= 1
                print(f"El contacto con el número de celular: '{celular}' ha sido eliminado.")
                return
        print(f"No se encontró contacto con el número de celular: {celular}")

    def eliminar_email(self, correo):
        """
        Elimina los datos de un contacto a partir del correo electronico.
        """
        self.ordenar_directorio()
        for persona in self.directorio:
            if persona and persona.email == correo:
                self.directorio.remove(persona)
                self.num_personas -= 1
                print(f"El contacto con el correo electrónico: '{correo}' ha sido eliminado.")
                return
            print(f"No se encontró contacto con el correo electrónico: {correo}")

    def buscar_contacto_celular(self, celular):
        '''
        Busca y muestra los contatos con un número de celular
        :param celular: Nombre de la carrera :str
        '''
        alumnos_cel = []
        profesores_cel= []
        coordinadores_cel = []

        for i in range(self.num_personas):
            if isinstance(self.directorio[i], cA.Alumno):
                if self.directorio[i].celular() == celular:
                    alumnos_cel.append(self.directorio[i])
            elif isinstance(self.directorio[i],cPr.Profesor):
                if self.directorio[i].celular() == celular:
                    profesores_cel.append(self.directorio[i])
            elif isinstance(self.directorio[i], cC.Coordinador):
                if self.directorio[i].celular() == celular:
                    coordinadores_cel.append(self.directorio[i])

        if alumnos_cel:
            print(f'Alumnos con el número de celular: {celular}:')
            for alumno in alumnos_cel:
                    print(alumno)
        else:
            print(f'No hay alumnos con el número de celular: {celular}')

        if profesores_cel:
            print(f'Profesores con el número de celular:{celular}:')
            for profesor in profesores_cel:
                print(profesor)
        else:
            print(f'No hay profesores con el número de celular: {celular}')

        if coordinadores_cel:
            print(f'Coordinadores de {celular}:')
            for coordinador in coordinadores_cel:
                    print(coordinador)
        else:
            print(f'No hay coordinadores con el número de celular: {celular}')

    def buscar_contacto_cum(self, cumpleaños):
        '''
        Busca y muestra los contatos respecto a una fecha de nacimiento
        :param cumpleaños: Nombre de la carrera :str
        '''
        alumnos_cum = []
        profesores_cum= []
        coordinadores_cum = []

        for i in range(self.num_personas):
            if isinstance(self.directorio[i], cA.Alumno):
                if self.directorio[i].fecha_cumpleanios() == cumpleaños:
                    alumnos_cum.append(self.directorio[i])
            elif isinstance(self.directorio[i],cPr.Profesor):
                if self.directorio[i].fecha_cumpleanios() == cumpleaños:
                    profesores_cum.append(self.directorio[i])
            elif isinstance(self.directorio[i], cC.Coordinador):
                if self.directorio[i].fecha_cumpleanios() == cumpleaños:
                    coordinadores_cum.append(self.directorio[i])

        if alumnos_cum:
            print(f'Alumnos con fecha de nacimiento: {cumpleaños}:')
            for alumno in alumnos_cum:
                    print(alumno)
        else:
            print(f'No hay alumnos con fecha de nacimiento: {cumpleaños}')

        if profesores_cum:
            print(f'Profesores con fecha de nacimiento:{cumpleaños}:')
            for profesor in profesores_cum:
                print(profesor)
        else:
            print(f'No hay profesores con fecha de nacimiento: {cumpleaños}')

        if coordinadores_cum:
            print(f'Coordinadores de {cumpleaños}:')
            for coordinador in coordinadores_cum:
                    print(coordinador)
        else:
            print(f'No hay coordinadores con fecha de nacimiento: {cumpleaños}')
