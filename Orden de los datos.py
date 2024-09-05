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

    def eliminar_cel(self, correo):
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
