from django.db import models

# Create your models here.
class Tema_Proyecto (models.Model):
    nombre_tema = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nombre_tema

class Persona (models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    documento_id = models.CharField(max_length = 100)
    correo = models.EmailField()
    telefono = models.PositiveIntegerField() 

    def __str__ (self):
        return self.nombre + " " + self.documento_id

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=5000)
    fecha_inico = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField()
    foto = models.ImageField( upload_to='proyectos', null=True, blank=True )
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    tema = models.ForeignKey(Tema_Proyecto, on_delete=models.PROTECT)

    def __str__ (self):
        return self.titulo + " " + self.persona.nombre
