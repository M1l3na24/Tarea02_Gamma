import copy
import numpy as np
import clasePersona as cP
import claseAlumno as cA
import claseProfesor as cPr
import claseCoordinador as cC

class Directorio:
    def __init__(self, almacenamiento):
        self.directorio = np.empty(almacenamiento, dtype=object)
        self.numeros_cuenta = set()
        self.numeros_profesor = set()
        self.numeros_empleado = set()
        self.num_personas = 0

    def __str__(self) -> str:
        cadena = ''
        self.ordenar_directorio()
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


    def ordenar_directorio(self):
        """Ordena el directorio por nombre"""
        self.directorio = sorted([p for p in self.directorio if p is not None], key=lambda x: x.nombre_completo)

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
        self.ordenar_directorio()
        for i, persona in enumerate(self.directorio):
            if persona is not None and persona.nombre_completo == nombre:
                self.directorio[i] = None
                self.num_personas -= 1
                print(f"Contacto '{nombre}' eliminado.")
                return
        print(f"No se encontró contacto con el nombre: {nombre}")

    def actualizar_contacto(self, nombre, nuevos_datos):
        """
        Actualiza la información de un contacto a partir del nombre.
        """
        for i, persona in enumerate(self.directorio):
            if persona is not None and persona.nombre_completo == nombre:
                self.directorio[i] = nuevos_datos
                print(f"Contacto '{nombre}' actualizado.")
                return
        print(f"No se encontró contacto con el nombre: {nombre}")

    def mostrar_contactos_por_sueldo(self, sueldo):
        """
        Muestra todos los contactos con un sueldo determinado.
        La información se muestra agrupada por categoría (profesor o coordinador).
        Los contactos se muestran ordenados.
        """
        profesores = []
        coordinadores = []
        self.ordenar_directorio()
        for persona in self.directorio:
            if isinstance(persona, cPr.Profesor) and persona.sueldo == sueldo:
                profesores.append(persona)
            elif isinstance(persona, cC.Coordinador) and persona.sueldo == sueldo:
                coordinadores.append(persona)

        if profesores:
            print("\nProfesores con sueldo determinado:")
            for profesor in profesores:
                print(profesor)
        else:
            print("\nNo se encontraron profesores con el sueldo especificado.")

        if coordinadores:
            print("\nCoordinadores con sueldo determinado:")
            for coordinador in coordinadores:
                print(coordinador)
        else:
            print("\nNo se encontraron coordinadores con el sueldo especificado.")

    def mostrar_contactos_con_email(self):
        '''
        Muestra los contactos por categoria y ordenados
        Obs: por como fue definido la clase Persona, todo objeto persona
        tiene un email valido.
        '''
        copia = copy.deepcopy(self)
        copia.eliminar_email(None)
        copia.eliminar_email('')
        print(copia)
        return

    def mostrar_contactos_de_carrera(self, carrera_particular):
        '''
        Muestra los contactos de una carrera particular
        :param carrera: Nombre de la carrera :str
        '''
        alumnos_en_carrera = []
        profesores_de_carrera = []
        coordinadores_de_carrera = []

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
        '''
        Muestra solo los alumnos o solo los maestros en orden
        Esto segun la eleccion del usuario
        :param eleccion: 0 si alumnos, 1 si maestros
        '''

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
