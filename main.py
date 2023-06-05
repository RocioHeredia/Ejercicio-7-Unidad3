from ClassLista import ListaPersonal
from ClassDocente import Docente
from ClassInvestigador import Investigador
from ClassDocenteInvestigador import DocenteInvestigador
from ClassPersonalApoyo import PersonaApoyo


def crear_agente():
    print("1. Docente")
    print("2. Investigador")
    print("3. Docente Investigador")
    print("4. Personal de Apoyo")
    tipo = int(input('Ingrese el tipo de Agente que desea Agregar: '))
    cuil = int(input("Ingrese el CUIL del agente: "))
    nombre = str(input("Ingrese el nombre del agente: "))
    apellido = str(input("Ingrese el apellido del agente: "))
    sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
    antiguedad = int(input("Ingrese la antigüedad del agente: "))
    if tipo == 1:
        carrera = input("Ingrese la carrera del docente: ")
        cargo = input("Ingrese el cargo del docente: ")
        catedra = input("Ingrese la cátedra del docente: ")
        docente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        retorna = docente
    elif tipo == 2:
        area_investigacion = str(input("Ingrese el área de investigación: "))
        tipo_investigacion = str(input("Ingrese el tipo de investigación: "))
        investigador = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion,
                                    tipo_investigacion)
        retorna = investigador
    elif tipo == 3:
        carrera = str(input("Ingrese la carrera del docente investigador: "))
        cargo = str(input("Ingrese el cargo del docente investigador: "))
        catedra = str(input("Ingrese la cátedra del docente investigador: "))
        area_investigacion = str(input("Ingrese el área de investigación: "))
        tipo_investigacion = str(input("Ingrese el tipo de investigación: "))
        categoria_incentivos = str(input("Ingrese la categoría en el programa de incentivos de investigación: "))
        importe_extra_doc = float(input("Ingrese el importe extra por docencia: "))
        docente_investigador = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo,
                                                   catedra, area_investigacion, tipo_investigacion, categoria_incentivos,
                                                   importe_extra_doc)
        retorna = docente_investigador
    elif tipo == 4:
        categoria = input("Ingrese la categoría del personal de apoyo: ")
        personal_apoyo = PersonaApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
        retorna = personal_apoyo
    else:
        print("Opción no válida.")
        retorna = None

    return retorna

def menu():
    print('OPCIONES')
    print('1. Insertar a agentes a la colección.')
    print('2. Agregar agentes a la coleccion.')
    print('3. Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.')
    print('4. Generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.')
    print('5. Cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.')
    print('6. Listado Ordenado por Apellido.')
    print('7. Listado de Docentes Investigadores por Categoria: ')
    print('8. Guardar en Archivo')
if __name__ == '__main__':
    lista = ListaPersonal()
    lista.LeerArchivoJson()
    #lista.mostrar_datos()
    opcion = None
    while opcion != 0:
        menu()
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            agente = crear_agente()
            posicion = int(input('Ingrese posicion en la que desea insertar al agente: '))
            lista.insertarPersonal(agente, posicion)
        elif opcion == 2:
            agente = crear_agente()
            lista.agregarPersonal(agente)
        elif opcion == 3:
            posicion = int(input('Ingrese posicion en la que desea insertar al agente: '))
            lista.mostrar_tipo(posicion)
        elif opcion == 4:
            nom_carrera = str(input('Ingrese nombre de la carrera: '))
            lista.listado_ordenado(nom_carrera)
        elif opcion == 5:
            area = str(input('Ingrese Area: '))
            lista.contarDocenteInEInvestigadores(area)
        elif opcion == 6:
            lista.generar_listado()
        elif opcion == 7:
            categoria = str(input('Ingrese Categoria: '))
            lista.listado_por_categoria(categoria)
        elif opcion == 8:
            lista.GuardarEnArchivoJson()
        else:
            opcion = int(input('Ingrese una opcion: '))
