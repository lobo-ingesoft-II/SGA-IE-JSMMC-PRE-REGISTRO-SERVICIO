class form_preRegsitro:
    def __init__(self, nombre:str, apellido:str, email:str, telefono:str, fecha_nacimiento:str, 
                 pais_nacimiento:str,departamento_nacimiento:str, municipio_nacimiento:str, 
                 categoria_sisben:str, subcategoria_sisben:str, direccion_residencia:str, seguro_medico:str,discapacidad:str,
                 detalle_discapacidad:str, poblacion_desplazada:str, fecha_desplazamiento:str, pais_residencia:str,
                 departamento_residencia:str, municipio_residencia:str, grado_ingreso:str, institucion_anterior:str,
                 municipio_anterior:str, sede:str, acudiente1_parentesco:str, acudiente1_apellidos:str,
                 acudiente1_nombres:str, acudiente1_cc:str, acudiente1_celular:str, acudiente1_ocupacion:str,
                 acudiente2_parentesco:str, acudiente2_apellidos:str, acudiente2_nombres:str,
                 acudiente2_cc:str, acudiente2_celular:str, acudiente2_ocupacion:str):
        
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.departamento_nacimiento = departamento_nacimiento
        self.municipio_nacimiento = municipio_nacimiento
        self.categoria_sisben = categoria_sisben
        self.subcategoria_sisben = subcategoria_sisben
        self.direccion_residencia = direccion_residencia
        self.seguro_medico = seguro_medico
        self.discapacidad = discapacidad
        self.detalle_discapacidad = detalle_discapacidad
        self.poblacion_desplazada = poblacion_desplazada
        self.fecha_desplazamiento = fecha_desplazamiento
        self.pais_residencia = pais_residencia
        self.departamento_residencia = departamento_residencia
        self.municipio_residencia = municipio_residencia
        self.grado_ingreso = grado_ingreso
        self.institucion_anterior = institucion_anterior
        self.municipio_anterior = municipio_anterior
        self.sede = sede
        self.acudiente1_parentesco = acudiente1_parentesco
        self.acudiente1_apellidos = acudiente1_apellidos
        self.acudiente1_nombres = acudiente1_nombres
        self.acudiente1_cc = acudiente1_cc
        self.acudiente1_celular = acudiente1_celular
        self.acudiente1_ocupacion = acudiente1_ocupacion
        self.acudiente2_parentesco = acudiente2_parentesco
        self.acudiente2_apellidos = acudiente2_apellidos
        self.acudiente2_nombres = acudiente2_nombres
        self.acudiente2_cc = acudiente2_cc
        self.acudiente2_celular = acudiente2_celular
        self.acudiente2_ocupacion = acudiente2_ocupacion

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "fecha_nacimiento": self.fecha_nacimiento,
            "pais_nacimiento": self.pais_nacimiento,
            "departamento_nacimiento": self.departamento_nacimiento,
            "municipio_nacimiento": self.municipio_nacimiento,
            "categoria_sisben": self.categoria_sisben,
            "subcategoria_sisben": self.subcategoria_sisben,
            "direccion_residencia": self.direccion_residencia,
            "seguro_medico": self.seguro_medico,
            "discapacidad": self.discapacidad,
            "detalle_discapacidad": self.detalle_discapacidad,
            "poblacion_desplazada": self.poblacion_desplazada,
            "fecha_desplazamiento": self.fecha_desplazamiento,
            "pais_residencia": self.pais_residencia,
            "departamento_residencia": self.departamento_residencia,
            "municipio_residencia": self.municipio_residencia,
            "grado_ingreso": self.grado_ingreso,
            "institucion_anterior": self.institucion_anterior,
            "municipio_anterior": self.municipio_anterior,
            "sede": self.sede,
            "acudiente1_parentesco": self.acudiente1_parentesco,
            "acudiente1_apellidos": self.acudiente1_apellidos,
            "acudiente1_nombres": self.acudiente1_nombres,
            "acudiente1_cc": self.acudiente1_cc,
            "acudiente1_celular": self.acudiente1_celular,
            "acudiente1_ocupacion": self.acudiente1_ocupacion,
            "acudiente2_parentesco": self.acudiente2_parentesco,
            "acudiente2_apellidos": self.acudiente2_apellidos,
            "acudiente2_nombres": self.acudiente2_nombres,
            "acudiente2_cc": self.acudiente2_cc,
            "acudiente2_celular": self.acudiente2_celular,
            "acudiente2_ocupacion": self.acudiente2_ocupacion
        }
        


# // Tipado del formulario
# type FormData = {
#   apellidos: string;
#   nombres: string;
#   tipoDocumento: string;
#   numeroDocumento: string;
#   fechaNacimiento: string;
#   paisNacimiento: string;
#   departamentoNacimiento: string;
#   municipioNacimiento: string;
#   categoriaSisben: string;
#   subcategoriaSisben: string;
#   direccionResidencia: string;
#   telefono: string;
#   rutaEscolar: string;
#   seguroMedico: string;
#   discapacidad: string;
#   detalleDiscapacidad: string;
#   poblacionDesplazada: string;
#   fechaDesplazamiento: string;
#   paisResidencia: string;
#   departamentoResidencia: string;
#   municipioResidencia: string;
#   gradoIngreso: string;
#   institucionAnterior: string;
#   municipioAnterior: string;
#   sede: string;
#   acudiente1Parentesco: string;
#   acudiente1Apellidos: string;
#   acudiente1Nombres: string;
#   acudiente1CC: string;
#   acudiente1Celular: string;
#   acudiente1Ocupacion: string;
#   acudiente2Parentesco: string;
#   acudiente2Apellidos: string;
#   acudiente2Nombres: string;
#   acudiente2CC: string;
#   acudiente2Celular: string;
#   acudiente2Ocupacion: string;
# };