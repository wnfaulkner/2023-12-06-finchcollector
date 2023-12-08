from django.db import models
from django.urls import reverse

CARGOS = (
  ('B', 'Beer'),
  ('C', 'Coconut'),
  ('D', 'Denisovan remains')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})
  

class Flight(models.Model):
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  date = models.DateField('flight date')
  cargo = models.CharField(
    max_length=1,
    choices=CARGOS,
    default=CARGOS[0][0],
  )
  def __str__(self):
    return f"{self.get_cargo_display()} on {self.date}"
  
  class Meta: #change the default sort
    ordering = ['-date']