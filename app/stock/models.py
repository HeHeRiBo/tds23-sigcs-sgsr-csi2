from django.db import models
from datetime import date

# Usando modelos de maestro, acoplado
from maestro.models import Institucion, Medicamento


class Lote(models.Model):
    codigo = models.CharField(max_length=250)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.codigo


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)

    """
    def save(self, *args, **kwargs):
        if self.cantidad < 0:
            raise IntegrityError("La cantidad de consumo debe ser mayor o igual que cero")

        super().save(*args, **kwargs)
    """


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    has_quiebre = models.BooleanField(default=False)
    fecha_actualizacion = models.DateField(default=date.today)

    def upd_cantidad(self):
        pass

    def upd_has_quiebre(self):
        pass

    def upd_caducidad(self):
        pass


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, unique=True)
    fecha = models.DateField(default=date.today)

    """
    class Meta:
        unique_together = ('institucion', 'lote')

    def save(self, *args, **kwargs):
        if Movimiento.objects.filter(lote=self.lote).exists():
            raise IntegrityError("UNIQUE constraint failed: stock_movimiento.lote_id")

        super().save(*args, **kwargs)
        """
