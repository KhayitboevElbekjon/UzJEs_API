from django.db import models
class Bolim(models.Model):
    nom=models.CharField(max_length=50)
    def __str__(self):
        return self.nom
class Sozlar(models.Model):
    bolim_fk=models.ForeignKey(Bolim,on_delete=models.CASCADE)
    nom=models.CharField(max_length=70)
    izhoh=models.TextField()
    gif=models.FileField()
    def __str__(self):
        return f"Bo'lim: {self.bolim_fk} | So'z nomi: {self.nom}"
