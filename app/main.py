# FastAPI es la clase principal con la que creamos la aplicación web.
from fastapi import FastAPI
# BaseModel permite describir la estructura de los datos recibidos.
# Field agrega reglas de validación y documentación a cada campo.
from pydantic import BaseModel, Field

# Este modelo representa el cuerpo JSON esperado en una inscripción.
# Pydantic validará estos datos antes de ejecutar el endpoint.
class Inscripcion(BaseModel):
    # El nombre debe llegar como texto.
    nombre: str
    # La edad debe ser un entero entre 0 y 120, inclusive.
    edad: int = Field(
        ge=0,
        le=120,
        description="Edad de la persona que solicita la inscripción"
    )
    # El curso también debe llegar como texto.
    curso: str
    # Creamos la aplicación y agregamos información descriptiva.
    # FastAPI utilizará estos datos en la documentación automática.

app = FastAPI(
        title="API de inscripciones",
        description="API educativa para validar inscripciones a cursos.",
        version="1.0.0"
    )

# Endpoint de bienvenida.
# El método GET se utiliza para consultar información.
@app.get("/")
def inicio() -> dict:
    # FastAPI convierte este diccionario en una respuesta JSON.
    return {
        "mensaje": "API de inscripciones en funcionamiento"
    }

# Endpoint sencillo para comprobar el estado del servicio.
# Más adelante podrá utilizarse como chequeo de salud.
@app.get("/status")
def obtener_estado() -> dict:
    return {
        "ok": True,
        "estado": "activo"
    }

# Endpoint que recibe información mediante POST.
# El parámetro inscripcion debe cumplir el modelo Inscripcion.
@app.post("/validar-inscripcion")
def validar_inscripcion(inscripcion: Inscripcion) -> dict:
    # Esta expresión produce un booleano: True o False.
    es_mayor: bool = inscripcion.edad >= 18
    # Aplicamos una regla de negocio diferente según la edad.
    if es_mayor:
        estado: str = "inscripción aceptada"
    else:
        estado = "requiere autorización de una persona adulta"
    # Devolvemos los datos recibidos junto con el resultado calculado.
    return {
        "ok": True,
        "nombre": inscripcion.nombre,
        "edad": inscripcion.edad,
        "curso": inscripcion.curso,
        "es_mayor": es_mayor,
        "estado": estado
    }