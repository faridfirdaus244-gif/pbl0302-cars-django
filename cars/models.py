from django.db import models

class Car(models.Model):
    carname = models.TextField()
    carbrand = models.TextField()
    carmodel = models.TextField()
    carprice = models.TextField()

    class Meta:
        db_table = 'tbcars'
        managed = False

    def __str__(self):
        return self.carname
