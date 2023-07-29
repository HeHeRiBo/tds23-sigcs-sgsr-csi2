from django.db import models
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from maestro.models import Institucion, Medicamento


class Lote(models.Model):
    codigo = models.CharField(max_length=250)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fecha_vencimiento = models.DateField()

    def __str__(self) -> str:
        return self.codigo


class Consumo(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha = models.DateField(default=date.today)


class Stock(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    has_quiebre = models.BooleanField(default=False)
    fecha_actualizacion = models.DateField(default=date.today)

    def upd_cantidad(self, cantidad):
        self.cantidad += cantidad
        self.save()

    def upd_has_quiebre(self):
        pass

    def upd_caducidad(self):
        pass


class Movimiento(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)


@receiver(post_save, sender=Movimiento)
def update_stock_after_movimiento(sender, instance, **kwargs):
    stock = Stock.objects.create(institucion=instance.institucion, medicamento=instance.lote.medicamento)

    stock = Stock.objects.all().first()
    stock.upd_cantidad(instance.lote.cantidad)
    stock.save()


@receiver(post_save, sender=Consumo)
def update_stock_after_consumo(sender, instance, **kwargs):
    stock = Stock.objects.create(institucion=instance.institucion, medicamento=instance.medicamento)

    stock = Stock.objects.all().first()
    stock.upd_cantidad(-instance.cantidad)
    stock.save()
