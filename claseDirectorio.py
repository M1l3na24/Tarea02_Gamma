# Programa: claseDirectorio.py
# Objetivo: Programa que define la clase Directorio
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 30-08-2024

import numpy as np

class Directorio:
    def __init__(self, almacenamiento):
        """
        Constructor que permite crear el objeto Directorio que sera
        un arreglo que contendra arreglos. Se construye como un directorio
        nuevo: vacio por default
        :param almacenamiento: indica el almacenamiento del directorio (0,n)
        """
        self.directorio = np.empty(almacenamiento, dtype=object)

    def insertar_nuevo_contacto(self, *params):
        """
        Constructor que permite crear diferentes objetos Persona
        :param params: Lista variable de parámetros (9 o 10)
        """

        self.alumnos = np.array()
        self.profesores = np.array()
        self.coordinadores = np.array()

