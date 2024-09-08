# Programa: MiDirectorio.py
# Autor: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Fecha: 09/09/2024
# Version: 1
# Descripcion: Programa que prueba el funcionamiento de la clase Directorio

import claseDirectorio as dir


def menuPrincipal() -> str:
    '''
    Metodo auxiliar que muestra un menu con todas las operaciones implementadas en
    el directorio escolar
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    '''
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Insertar datos de un nuevo contacto\n'
                       '2. Mostrar información de un contacto\n'
                       '3. Eliminar información de un contacto\n'
                       '4. Actualizar los datos de un contacto \n'
                       'S. Guardar y Salir \n').upper()
        if opcion not in '1,2,3,4,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menuInsertarDatos() -> str:
    '''
    Metodo auxiliar que despliega las opciones que podemos realizar al insertar los datos de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    '''
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Agregar Alumno\n'
                       '2. Agregar Profesor\n'
                       '3. Agregar Coordinador\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menuActualizar():
    '''
    Metodo auxiliar que despliega las opciones que podemos realizar al actualizar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    '''
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Actualizar Alumno\n'
                       '2. Actualizar Profesor\n'
                       '3. Actualizar Coordinador\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menuEliminar():
    '''
    Metodo auxiliar que despliega las opciones que podemos realizar al eliminar
    un contacto
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    '''
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Borrar contacto a partir del nombre\n'
                       '2. Borrar contacto a partir del número de celular\n'
                       '3. Borrar contacto a partir del correo electrónico\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


def menuMostrarInfo():
    '''
    Metodo auxiliar que despliega las opciones que podemos realizar al mostrar información de los contactos
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    '''
    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Mostrar por nombre\n'
                       "2. Mostrar por nombre y rol\n"
                       "3. Mostrar por sueldo\n"
                       "4. Mostrar por correo electronico\n"
                       "5. Mostrar por carrera\n"
                       "6. Mostrar por alumnos o profesores\n"
                       "7. Mostrar por cumpleaños"
                       "8. Mostrar por número de celular\n"
                       'S. Salir \n').upper()
        if opcion not in '1,2,3,4,5,6,7,8,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcion


if __name__ == "__main__":
    print("Bienvenido al Directorio, donde se podra administrar los contactos de la escuela")

    while True:
        try:
            almacenamiento = int(input('Escriba el tamaño del directorio: '))
            break
        except ValueError:
            print('El tamanño de directorio debe ser entero')

    directorio = dir.Directorio(almacenamiento)

    while True:
        opcion = input('Que deseas hacer:\n'
                       '1. Cargar información del directorio\n'
                       '2. Crear información nueva del directorio\n'
                       'S. Salir \n').upper()
        if opcion not in '1,2,S' or len(opcion) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    match opcion:
        case '1':
            dir.lectura_csvs()
            opcion = ''
            while opcion != 'S':
                opcion = menuPrincipal()
                match opcion:
                    case "1":
                        while opcion != 'S':
                            opcion = menuInsertarDatos()
                            match opcion:
                                case '1':
                                    directorio.insertar_nuevo_alumno()
                                case '2':
                                    directorio.insertar_nuevo_profesor()
                                case '3':
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = " "
                    case '2':
                        while opcion != 'S':
                            opcion = menuMostrarInfo()
                            match opcion:
                                case '1':
                                    directorio.mostrar_persona()
                                #case '2':
                                    #directorio.()
                                #case '3':
                                    #directorio.()
                                #case "4":
                                    #directorio.()
                                #case '5':
                                    #directorio.()
                                #case '6':
                                    #directorio.()
                                case '7':
                                    directorio.buscar_contacto_cum()
                                case "8":
                                    directorio.buscar_contacto_celular()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case '3':
                        while opcion != 'S':
                            opcion = menuEliminar()
                            match opcion:
                                #case '1':
                                    #directorio.()
                                case '2':
                                    directorio.eliminar_cel()
                                case '3':
                                    directorio.eliminar_email()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case '4':
                        while opcion != 'S':
                            opcion = menuActualizar()
                            match opcion:
                                #case '1':
                                    #directorio.()
                                #case '2':
                                    #directorio.()
                                #case '3':
                                    #directorio.()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case 'S':
                        dir.guardar_Archivo()
                        print("Hasta luego")
        case '2':
            opcion = ''
            while opcion != 'S':
                opcion = menuPrincipal()
                match opcion:
                    case "1":
                        while opcion != 'S':
                            opcion = menuInsertarDatos()
                            match opcion:
                                case '1':
                                    directorio.insertar_nuevo_alumno()
                                case '2':
                                    directorio.insertar_nuevo_profesor()
                                case '3':
                                    directorio.insertar_nuevo_coordinador()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ""
                    case '2':
                        while opcion != 'S':
                            opcion = menuMostrarInfo()
                            match opcion:
                                case '1':
                                    directorio.mostrar_persona()
                                #case '2':
                                    #directorio.()
                                #case '3':
                                    #directorio.()
                                #case "4":
                                    #directorio.()
                                #case '5':
                                    #directorio.()
                                #case '6':
                                    #directorio.()
                                case '7':
                                    directorio.buscar_contacto_cum()
                                case "8":
                                    directorio.buscar_contacto_celular()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case '3':
                        while opcion != 'S':
                            opcion = menuEliminar()
                            match opcion:
                                #case '1':
                                    #directorio.()
                                case '2':
                                    directorio.eliminar_cel()
                                case '3':
                                    directorio.eliminar_email()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case '4':
                        while opcion != 'S':
                            opcion = menuActualizar()
                            match opcion:
                                #case '1':
                                    #directorio.()
                                #case '2':
                                    #directorio.()
                                #case '3':
                                    #directorio.()
                                case 'S':
                                    print('Regresando al menu principal')
                        opcion = ''
                    case 'S':
                        dir.guardar_Archivo()
                        print("Hasta luego")
        case 'S':
            print('Hasta luego')