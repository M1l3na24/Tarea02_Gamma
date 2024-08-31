# Programa: claseProfesor.py
# Objetivo: Clase que modela un Profesor que hereda de Persona
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Fecha: 31-08-2024

import clasePersona as cP
from datetime import date
from locale import currency, setlocale, LC_MONETARY


class Profesor(cP.Persona):
    """
    Clase que representa una persona del tipo Profesor.
    """

    def __init__(self, nombre_completo: str, celular: str, fecha_cumpleanios: date, email: str, num_profesor: int,
                 tel_oficina: int, sueldo:int, dept_ads: str, carrera: str, grupos: list):
        """
        Constructor para un Profesor, ademas de los datos de una Persona, recibe el numero de profesor,
        telefono de oficina, sueldo, departamento de adscripcion, carrera donde imparte materias,
        y grupos.
        :param nombre_completo: El nombre completo del Profesor
        :param celular: El celular del Profesor
        :param fecha_cumpleanios: La fecha de cumpleanios del Profesor
        :param email: EL correo electronico del Profesor
        :param num_profesor: El numero de profesor
        :param tel_oficina: El telefono del Profesor
        :param sueldo: El sueldo del Profesor
        :param dept_ads: El departamento del Profesor
        :param carrera: La carrera donde imparte materias el Profesor
        :param grupos: Los grupos del Profesor
        """
        super().__init__(nombre_completo, celular, fecha_cumpleanios, email)
        self.__num_profesor = num_profesor
        self.__tel_oficina = tel_oficina
        self.__sueldo = sueldo
        self.__dept_ads = dept_ads
        self.__carrera = carrera
        self.__grupos = grupos


    # Metodos GET
    @property
    def num_profesor(self) -> int:
        """
        Metodo para obtener el numero de profesor del Profesor
        :return: El numero de profesor
        :rtype: int
        """
        return self.__num_profesor

    @property
    def tel_oficina(self) -> int:
        """
        Metodo para obtener el numero de oficina del Profesor
        :return: El numero de oficina
        :rtype: int
        """
        return self.__tel_oficina

    @property
    def sueldo(self) -> int:
        """
        Metodo para obtener el sueldo del Profesor
        :return: El sueldo del profesor
        :rtype: int
        """
        return self.__sueldo
    @property
    def dept_ads(self) -> str:
        """
        Metodo para obtener el departamento de adscripcion del Profesor
        :return: El departamento de adscripcion del profesor
        :rtype: str
        """
        return self.__dept_ads

    @property
    def carrera(self) -> str:
        """
        Metodo para obtener la carrera donde imparte materias el Profesor
        :return: La carrera donde imparte materias el Profesor
        :rtype: str
        """
        return self.__carrera

    @property
    def grupos(self) -> list:
        """
        Metodo para obtener la lista de grupos del Profesor
        :return: La lista de grupos del Profesor
        :rtype: list
        """
        return self.__grupos


    # Metodos SET
    @num_cuenta.setter
    def num_cuenta(self, num_cuenta: int):
        """
        Metodo para modificar el numero de cuenta del Alumno
        :param num_cuenta: El numero de cuenta del Alumno
        """
        self.__num_cuenta = num_cuenta

    @carrera.setter
    def carrera(self, carrera: str):
        """
        Metodo para modificar la carrera del Alumno
        :param carrera: La carrera del Alumno
        """
        self.__carrera = carrera

    @materias.setter
    def materias(self, materias: list):
        """
        Metodo para modificar las materias del Alumno
        :param materias: La lista de materias del Alumno
        """
        self.__materias = materias

    @semestre.setter
    def semestre(self, semestre: int):
        """
        Metodo para modificar el semestre del Alumno
        :param semestre: El semestre del Alumno
        """
        self.__semestre = semestre

    # Metodos calculadores
    def __str__(self) -> str:
        """
        Metodo para obtener un Alumno en formato cadena
        :return: El Alumno en formato de impresion
        :rtype: str
        """
        return super().__str__().replace("Persona", "Alumno") + \
            " | Num_cuenta: {} | Carrera: {} | Materias: {} | Semestre: {} |".format(self.__num_cuenta,
                                                                                     self.__carrera, self.__materias,
                                                                                     self.__semestre)

    # Este metodo se define cuando se desea que los objetos se guarden en un archivo

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de un objeto
        :return: La representacion en formato iterable del Alumno
        :rtype: iterable
        """
        return iter([super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email,
                     self.__num_cuenta, self.__carrera, self.__materias, self.__semestre])

    # Estos metodos se tienen que agregar cuando se trabajan con objetos en los Conjuntos y lograr
    # que sus objetos sean hasheables

    def __llave(self) -> tuple:
        """
        Metodo privado que permite definir una llave a través de los atributos del objeto
        :return: Una tupla con los atributos del objeto.
        :rtype: tuple
        """
        return (super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email, self.__num_cuenta,
                self.__carrera, self.__materias, self.__semestre)

    def __hash__(self) -> int:
        """
        Metodo que internamente llama la funcion hash() para obtener el valor hash del objeto.
        Se utilizan generalmente para una comparacion mas rapida entre los dos objetos,
        ya que los valores hash se comparan directamente en lugar de comparar el valor de cada objeto.
        :return: Un valor entero que corresponde al valor hash del objeto
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Metodo que permite definir el criterio de igualdad para dos objetos
        :param otro: El Alumno con el que se va a realizar la comparacion
        :return: True si los Alumnos son iguales, False en caso contrario
        :rtype: bool
        """
        if isinstance(otro, Alumno):
            return self.__llave() == otro.__llave()
