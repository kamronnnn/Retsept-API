from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Retsept(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    retsept = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.CharField(max_length=15)
    grade = models.IntegerField(default=0, verbose_name='1 - 5')

    def __str__(self):
        return self.user




