from django.db import models


class Kinodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Kino"


class Rekinodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Rekino"


class Chanchitodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Chanchito"


class Combodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Combo"


class Chao1db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Chao Jefe 1"


class Chao2db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Chao Jefe 2"


class Chao3db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"Chao Jefe 3"


class Archivosxl(models.Model):
    file = models.FileField(upload_to='excels')

    def delete(self):
        self.file.delete()
        super().delete()
