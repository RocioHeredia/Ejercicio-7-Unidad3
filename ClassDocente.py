from ClassPersonal import Personal
class Docente(Personal):

    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria=None, area_investigacion=None,
                 tipo_investigacion=None):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera_dicta, cargo, catedra, categoria, area_investigacion, tipo_investigacion)
        self.__carrera_dicta = str(carrera_dicta)
        self.__cargo = str(cargo)
        self.__catedra = str(catedra)

    def mostrar(self):
        cadena = super().mostrar()
        cadena += f'Carrera que Dicta:{self.__carrera_dicta}\n'
        cadena += f'Cargo:{self.__cargo}\n'
        cadena += f'Catedra:{self.__catedra}\n'
        return cadena

    def get_carrera(self):
        return self.__carrera_dicta

    def calcular_sueldo(self):
        global porcentaje_por_cargo
        sueldo = super().calcular_sueldo()
        if str(self.__cargo) == 'simple':
            porcentaje_por_cargo = 0.1
        elif str(self.__cargo) == 'semiexclusivo':
            porcentaje_por_cargo = 0.2
        elif str(self.__cargo) == 'exclusivo':
            porcentaje_por_cargo = 0.5
        sueldo_total = sueldo + (float(super().get_sueldo_basico()) * porcentaje_por_cargo)

        return sueldo_total

    def diccionario(self):
        personal_dic = super().diccionario()
        personal_dic["carrera"] = self.__carrera_dicta
        personal_dic["cargo"] = self.__cargo
        personal_dic["catedra"] = self.__catedra
        return personal_dic
