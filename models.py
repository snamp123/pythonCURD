from django.db import models

class Employeespython(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)

    class Meta:
        db_table = 'employeespython'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
